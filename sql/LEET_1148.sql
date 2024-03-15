# Write your MySQL query statement below
SELECT DISTINCT author_id as id from Views 
WHERE Views.author_id = Views.viewer_id
ORDER BY author_id ASC

