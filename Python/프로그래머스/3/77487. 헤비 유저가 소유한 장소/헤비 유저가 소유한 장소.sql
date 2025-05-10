-- 코드를 입력하세요
WITH cte AS (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING count(HOST_ID) >= 2
)
SELECT p.ID
      ,p.NAME
      ,p.HOST_ID
FROM PLACES p
WHERE p.HOST_ID IN (SELECT * FROM cte)