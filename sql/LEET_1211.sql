# Write your MySQL query statement below
SELECT 
    q.query_name, 
    ROUND(SUM(q.rating / q.position) / COUNT(*), 2) quality, 
    ROUND(SUM(CASE WHEN q.rating < 3 THEN 100 ELSE 0 END) / COUNT(*), 2) poor_query_percentage 
FROM Queries q
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name