-- 1. Candidates Table
CREATE TABLE IF NOT EXISTS Candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE
);

-- 2. Departments Table
CREATE TABLE IF NOT EXISTS Departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL UNIQUE,
    budget_allocation REAL
);

-- 3. Applications Table (The Link Table)
CREATE TABLE IF NOT EXISTS Applications (
    app_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER,
    dept_id INTEGER,
    applied_date TEXT,
    status TEXT DEFAULT 'Pending',
    salary_expected REAL,
    FOREIGN KEY (candidate_id) REFERENCES Candidates(candidate_id),
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);