SELECT c.CAR_ID, c.CAR_TYPE, ROUND(30*c.DAILY_FEE*(1-dp.DISCOUNT_RATE/100)) as FEE
FROM CAR_RENTAL_COMPANY_CAR c JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp USING(CAR_TYPE)
WHERE c.CAR_TYPE IN ('세단', 'SUV')
    AND
      dp.DURATION_TYPE = '30일 이상'
    AND
      CAR_ID NOT IN (SELECT CAR_ID
                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01')
    AND (ROUND(30*c.DAILY_FEE*(1-dp.DISCOUNT_RATE/100)) >= 500000 AND ROUND(30*c.DAILY_FEE*(1-dp.DISCOUNT_RATE/100)) < 2000000 )