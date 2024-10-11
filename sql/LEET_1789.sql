# Write your MySQL query statement below

SELECT e1.employee_id, IFNULL(MIN(e2.department_id), e1.department_id) department_id   
FROM Employee e1
LEFT JOIN (
    SELECT employee_id, department_id
    FROM Employee
    WHERE primary_flag = 'Y'
) e2
ON e1.employee_id = e2.employee_id and e1.department_id = e2.department_id
GROUP BY employee_id
