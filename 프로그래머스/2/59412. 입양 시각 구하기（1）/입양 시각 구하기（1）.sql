# -- 코드를 입력하세요
# WITH TLB AS (
#     SELECT *, CASE
#             WHEN TIME(DATETIME) BETWEEN "09:00" AND "09:59" THEN "9"
#             WHEN TIME(DATETIME) BETWEEN "10:00" AND "10:59" THEN "10"
#             WHEN TIME(DATETIME) BETWEEN "11:00" AND "11:59" THEN "11"
#             WHEN TIME(DATETIME) BETWEEN "12:00" AND "12:59" THEN "12"
#             WHEN TIME(DATETIME) BETWEEN "13:00" AND "13:59" THEN "13"
#             WHEN TIME(DATETIME) BETWEEN "14:00" AND "14:59" THEN "14"
#             WHEN TIME(DATETIME) BETWEEN "15:00" AND "15:59" THEN "15"
#             WHEN TIME(DATETIME) BETWEEN "16:00" AND "16:59" THEN "16"
#             WHEN TIME(DATETIME) BETWEEN "17:00" AND "17:59" THEN "17"
#             WHEN TIME(DATETIME) BETWEEN "18:00" AND "18:59" THEN "18"
#             WHEN TIME(DATETIME) BETWEEN "19:00" AND "19:59" THEN "19"
#            END AS HOUR
#     FROM ANIMAL_OUTS
#     WHERE HOUR(DATETIME) BETWEEN 9 AND 19
# )

SELECT HOUR(DATETIME), COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)