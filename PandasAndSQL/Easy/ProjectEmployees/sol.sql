# Write your MySQL query statement below
SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
#then groupby final result
GROUP BY project_id
