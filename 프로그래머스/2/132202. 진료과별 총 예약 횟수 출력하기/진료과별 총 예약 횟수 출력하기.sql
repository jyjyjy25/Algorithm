# SELECT MCDP_CD as '진료과 코드', COUNT(*) as '5월예약건수'
# FROM APPOINTMENT
# WHERE APNT_YMD LIKE '2022-05%' AND APNT_CNCL_YN = 'N'
# GROUP BY MCDP_CD
# ORDER BY '5월예약건수', '진료과 코드'


SELECT MCDP_CD AS 진료과코드, COUNT(MCDP_CD) AS 5월예약건수
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') LIKE '2022-05%'
GROUP BY 진료과코드
ORDER BY 5월예약건수 ASC, 진료과코드 ASC