# Write your MySQL query statement below
SELECT r.contest_id, ROUND(count(*)*100 / (SELECT Count(*) FROM Users) , 2) percentage 
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id 