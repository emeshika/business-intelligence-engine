# Optimizing Recruitment Decision-Making: End-to-End Relational Database & Data Pipeline 📊🗄️

## Project Overview
This project represents a comprehensive data engineering initiative dedicated to transforming messy, unstructured candidate and application logs into a professional, high-performance relational database environment. By replacing flat-file storage with a standardized SQL infrastructure, this system bridges the gap between raw corporate data entry and high-level, actionable business intelligence for human capital allocation.

The core objective is to build a scalable and error-resilient data migration pipeline that establishes a "Single Source of Truth" while evaluating departmental financial indices and recruitment funnel bottlenecks.

## Key Features
* **Automated Data Preprocessing Engine:** Uses Python to automatically capture and purge logical redundancies (de-duplication), resolve administrative omissions via statistical mean profiling, and standardize inconsistent date-entry formats.
* **Professional Relational Architecture:** Logically maps normalized records into a 3-table relational model (*Candidates, Departments, and Applications*) utilizing Primary and Foreign Key constraints under Third Normal Form (3NF) principles.
* **Executive Data Analytics Layer:** Leverages advanced multi-table SQL JOIN operations to parse isolated business segments into immediate operational insights (e.g., regional salary benchmarking and real-time candidate funnel sorting).
* **Enterprise Security & Portability Layout:** Incorporates strict decoupled environment variables (`.env`) and version-control boundaries (`.gitignore`) to prevent internal candidate data leaks while maintaining portability.

## Project Architecture & Pipeline
1. **Synthetic Data Generation Strategy (`generate_raw_data.py`):** Programmatically constructs an experimental dataset of 100+ multi-attribute candidate profiles containing intentional administrative anomalies (noise, multi-format timestamps, null records) to stress-test pipeline resiliency.
2. **The Cleaning & Normalization Pipeline (`cleaning_script.py`):** Standardizes textual properties, updates incomplete candidate states to baseline fallbacks, and executes categorical groupings.
3. **Database Architecture Migration (`database_setup.sql`):** Instantiates a lightweight, zero-configuration **SQLite engine** and maps the cleared Pandas structures into database schemas.
4. **Insight Synthesis (`analysis_queries.sql`):** Runs advanced analytical metrics assessing premium-tier tech role allocations and pipeline aging trends.

## Tech Stack
* **Language:** Python 3.12, Structured Query Language (SQL)
* **Data Manipulation & Ingestion:** Pandas, NumPy
* **Database Management System:** SQLite 3 (`business_vault.db`)
* **Development Workspace & Tools:** Visual Studio Code, Python Virtual Environments (`venv`), Git

## Strategic Business Insights Delivered
* **Departmental Premium Tracking:** Located high-cost hiring metrics concentrated heavily within **Marketing (107,397.81 LKR average expectation)** and **Data Science (106,093.90 LKR average expectation)** divisions.
* **Funnel Optimization Benchmarks:** Structured immediate cohort filters mapping pipeline states (*Hired, Rejected, Pending, Under Review*) to automate age-alerts for premium applications stalled beyond 30 days.
* **Data Fidelity Optimization:** Successfully purged redundant entries, reducing administrative inventory noise down to exactly **100 high-fidelity unique candidate records**.
