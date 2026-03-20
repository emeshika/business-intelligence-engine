import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv("DB_NAME", "business_vault.db")

def process_normalized_data():
    # Load raw data
    df = pd.read_csv('data/raw_business_data.csv')
    df = df.drop_duplicates()

    # Standardize dates (supports both YYYY-MM-DD and DD/MM/YYYY)
    raw_dates = df['applied_date']
    parsed = pd.to_datetime(raw_dates, errors='coerce', dayfirst=False)
    if parsed.isna().any():
        parsed = parsed.fillna(pd.to_datetime(raw_dates, errors='coerce', dayfirst=True))
    invalid_count = parsed.isna().sum()
    if invalid_count:
        print(f"Warning: {invalid_count} row(s) have invalid applied_date values and will be left blank.")
    df['applied_date'] = parsed.dt.strftime('%Y-%m-%d')

    df['status'] = df['status'].fillna('Under Review')
    df['salary_expected'] = df['salary_expected'].fillna(df['salary_expected'].mean())

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 1. Populate Departments (Unique list)
    depts = pd.DataFrame(df['department'].dropna().unique(), columns=['dept_name'])
    depts = depts.reset_index(drop=True)
    depts['dept_id'] = depts.index + 1
    depts['budget_allocation'] = 500000  # Default budget for example
    depts.to_sql('Departments', conn, if_exists='replace', index=False)

    # 2. Populate Candidates
    candidates = df[['candidate_name']].drop_duplicates().copy()
    candidates = candidates.rename(columns={'candidate_name': 'full_name'})
    candidates = candidates.reset_index(drop=True)
    candidates['candidate_id'] = candidates.index + 1
    candidates['email'] = candidates['full_name'].str.replace(' ', '.').str.lower() + "@example.com"
    candidates.to_sql('Candidates', conn, if_exists='replace', index=False)

    # 3. Populate Applications (Merging IDs)
    # Re-fetch IDs to ensure mapping is correct
    db_depts = pd.read_sql('SELECT dept_id, dept_name FROM Departments', conn)
    db_cands = pd.read_sql('SELECT candidate_id, full_name FROM Candidates', conn)

    final_apps = df.merge(db_cands, left_on='candidate_name', right_on='full_name')
    final_apps = final_apps.merge(db_depts, left_on='department', right_on='dept_name')

    final_apps[['candidate_id', 'dept_id', 'applied_date', 'status', 'salary_expected']].to_sql(
        'Applications', conn, if_exists='replace', index=False
    )

    conn.close()
    print("Database normalized and loaded into 3 tables!")

if __name__ == "__main__":
    process_normalized_data()