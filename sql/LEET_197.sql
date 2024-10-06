# Write your MySQL query statement below
SELECT cur.id 
FROM Weather cur
JOIN Weather prev on cur.recordDate = DATE_ADD(prev.recordDate, INTERVAL 1 DAY)
WHERE cur.temperature > prev.temperature;