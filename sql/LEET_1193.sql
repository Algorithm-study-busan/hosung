# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(t.trans_date, '%Y-%m') month, 
    t.country,
    COUNT(*) trans_count,
    COUNT(CASE WHEN t.state = 'approved' THEN 1 ELSE null END) approved_count,
    SUM(t.amount) trans_total_amount ,
    SUM(CASE WHEN t.state = 'approved' THEN t.amount ELSE 0 END) approved_total_amount 
FROM Transactions t
GROUP BY month, t.country
