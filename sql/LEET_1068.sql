# Write your MySQL query statement below
SELECT product_name, year, price 
FROM Product 
JOIN Sales on Product.product_id = Sales.product_id;