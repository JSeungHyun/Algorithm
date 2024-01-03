-- 코드를 입력하세요
# WITH truck AS (
#     SELECT CAR_ID, DAILY_FEE
#     FROM CAR_RENTAL_COMPANY_CAR
#     WHERE CAR_TYPE = '트럭'
# ),
# cte AS (
#     SELECT CAR_ID 
#       ,CASE
#            WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 7 AND 29
#            THEN '7일 이상'
#            WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 30 AND 89
#            THEN '30일 이상'
#            WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90
#            THEN '90일 이상'
#         END AS DURATION_TYPE
#      ,HISTORY_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE CAR_ID IN (SELECT CAR_ID FROM truck)
# )

# SELECT h.HISTORY_ID
#       ,CASE
#            WHEN DISCOUNT_RATE IS NULL
#            THEN DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1)
#            ELSE ROUND((DAILY_FEE * (1 - DISCOUNT_RATE / 100)) * (DATEDIFF(END_DATE, START_DATE) + 1))
#        END AS FEE
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
# INNER JOIN cte c
#         ON h.HISTORY_ID = c.HISTORY_ID
# INNER JOIN truck t
#         ON t.CAR_ID = h.CAR_ID
# LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
#        ON p.DURATION_TYPE = c.DURATION_TYPE
#       AND p.CAR_TYPE = '트럭'
# ORDER BY 2 DESC, 1 DESC

SELECT DISTINCT HISTORY_ID
               ,FEE
FROM
    (SELECT CH.history_id as HISTORY_ID
           ,DATEDIFF(end_date, start_date) AS 'DATE_DIFF'
           ,CASE 
                WHEN (DATEDIFF(end_date, start_date)+1 BETWEEN 7 AND 29) AND duration_type = '7일 이상' THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date)+1 BETWEEN 30 AND 89) AND duration_type = '30일 이상' THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date)+1 >= 90) AND duration_type = '90일 이상' THEN ROUND(daily_fee *(DATEDIFF(end_date, start_date)+1) * (100 - discount_rate) * 0.01)
                WHEN (DATEDIFF(end_date, start_date) < 7)  THEN ROUND(daily_fee * (DATEDIFF(end_date, start_date)+1))
                ELSE NULL
           END AS 'FEE'
    FROM CAR_RENTAL_COMPANY_CAR AS CR
         LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CH ON CR.car_id = CH.car_id
         LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS CP ON CR.car_type = CP.car_type
    WHERE CR.car_type = '트럭'
    ) AS TEMP
WHERE FEE IS NOT NULL
ORDER BY FEE DESC, history_id DESC