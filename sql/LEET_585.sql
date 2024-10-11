# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) tiv_2016
FROM Insurance
WHERE 
    pid not in (
        SELECT pid
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) = 1
    )
    and
    pid in (
        SELECT pid 
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    )