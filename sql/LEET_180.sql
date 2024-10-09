# Write your MySQL query statement below
SELECT DISTINCT l1.num ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id-1 
JOIN Logs l3 ON l2.id = l3.id-1
WHERE l1.num = l2.num and l2.num = l3.num;