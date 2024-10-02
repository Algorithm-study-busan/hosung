# Write your MySQL query statement below
SELECT customer_id, count(*) count_no_trans
FROM Visits 
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id is null
Group by customer_id;