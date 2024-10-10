# Write your MySQL query statement below
SELECT id, SUM(cnt) num
FROM 
((
    SELECT requester_id id, COUNT(*) cnt 
    FROM RequestAccepted 
    GROUP BY requester_id
)
UNION ALL
(
    SELECT accepter_id id, COUNT(*) cnt 
    FROM RequestAccepted 
    GROUP BY accepter_id
)) t
GROUP BY id
ORDER BY num DESC
limit 1
