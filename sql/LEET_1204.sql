WITH q AS (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) total
    FROM Queue
)

SELECT person_name
FROM q
WHERE total <= 1000 and total = (SELECT MAX(total) FROM q WHERE total <= 1000)
