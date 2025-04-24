-- 코드를 입력하세요
WITH TLB AS (
    SELECT 
        *,
        CASE
            WHEN START_DATE < "2022-10-16" AND END_DATE < "2022-10-16" THEN "대여 가능"
            WHEN START_DATE <= "2022-10-16" AND END_DATE >= "2022-10-16" THEN "대여중"
            ELSE "대여 가능"
        END AS AVAILABILITY1
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

SELECT
    CAR_ID,
    CASE
       WHEN SUM(AVAILABILITY1 = '대여중') > 0 THEN '대여중'
        ELSE '대여 가능'
    END AS ASAVAILABILITY
FROM 
    TLB
GROUP BY 
    CAR_ID
ORDER BY 
    CAR_ID DESC