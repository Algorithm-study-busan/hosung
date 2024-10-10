# Write your MySQL query statement below
WITH c as (
    SELECT customer_id, visited_on, SUM(amount) amount
    FROM Customer
    GROUP BY visited_on
)

SELECT c1.visited_on, SUM(c2.amount) amount, ROUND(AVG(c2.amount),2) average_amount
FROM c c1
JOIN c c2 ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 day) and c1.visited_on
GROUP BY c1.visited_on
HAVING COUNT(*) = 7
ORDER BY c1.visited_on