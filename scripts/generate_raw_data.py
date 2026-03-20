import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Ensure data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Settings
departments = ['Data Science', 'Software Engineering', 'HR', 'Marketing', 'Finance']
statuses = ['Hired', 'Rejected', 'Interview', 'Pending', None]
names = ['Amara', 'Saman', 'Hirushi', 'Nimal', 'Priya', 'Kavindi', 'Sunil', 'Deepika', 'Arjun', 'Nilanthi']

data = []
for i in range(1, 101):
    name = f"{random.choice(names)} {random.choice(['Silva', 'Perera', 'Fernando', 'Kumara'])}"
    base_date = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 60))
    date_str = base_date.strftime('%d/%m/%Y') if i % 10 == 0 else base_date.strftime('%Y-%m-%d')
        
    data.append({
        'id': i,
        'candidate_name': name,
        'applied_date': date_str,
        'department': random.choice(departments),
        'status': random.choice(statuses),
        'salary_expected': random.randint(50000, 150000) if i % 15 != 0 else None
    })

df = pd.DataFrame(data)
df = pd.concat([df, df.head(5)], ignore_index=True)

# This creates the CSV file for you
df.to_csv('data/raw_business_data.csv', index=False)
print("Generated raw_business_data.csv with 105 rows in the data folder!")