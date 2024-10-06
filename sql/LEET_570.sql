# Write your MySQL query statement below
SELECT t.name
FROM 
(
    SELECT e1.name, count(e2.managerId) cnt
    FROM Employee e1 
    JOIN Employee e2 on e1.id = e2.managerId
    GROUP BY e2.managerId
) as t
WHERE t.cnt >= 5