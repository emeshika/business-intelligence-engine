-- INSIGHT: Average salary per department using a JOIN
SELECT d.dept_name, ROUND(AVG(a.salary_expected), 2) as avg_salary
FROM Applications a
JOIN Departments d ON a.dept_id = d.dept_id
GROUP BY d.dept_name;

-- INSIGHT: List all Hired candidates and their departments
SELECT c.full_name, d.dept_name, a.status
FROM Applications a
JOIN Candidates c ON a.candidate_id = c.candidate_id
JOIN Departments d ON a.dept_id = d.dept_id
WHERE a.status = 'Hired';