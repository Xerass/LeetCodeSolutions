SELECT 
    Department.name as Department, 
    Employee.name as Employee, 
    Employee.salary as Salary
FROM 
    Employee
JOIN 
    Department ON Employee.departmentId = Department.id
WHERE 
    (Employee.departmentId, Employee.salary) IN (
        SELECT 
            departmentId, MAX(salary)
        FROM 
            Employee
        GROUP BY 
            departmentId
    );
