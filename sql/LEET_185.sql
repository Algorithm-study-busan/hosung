# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT 
        e.name as Employee, 
        e.salary as Salary, d.name as Department, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY Salary DESC) as num
    FROM Employee e
    JOIN Department d ON e.departmentId  = d.id
) t
WHERE num <= 3