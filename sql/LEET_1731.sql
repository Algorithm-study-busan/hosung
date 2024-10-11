# Write your MySQL query statement below
SELECT e1.employee_id, e1.name, COUNT(*) reports_count, ROUND(AVG(e2.age),0) average_age 
FROM Employees e1
JOIN Employees e2 on e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY e1.employee_id