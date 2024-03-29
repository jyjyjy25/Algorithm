-- 코드를 입력하세요
SELECT fp.PRODUCT_ID, fp.PRODUCT_NAME, SUM(AMOUNT) * PRICE as TOTAL_SALES
FROM FOOD_PRODUCT fp JOIN FOOD_ORDER fo USING (PRODUCT_ID)
WHERE PRODUCE_DATE LIKE '2022-05%'
GROUP BY fp.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, fp.PRODUCT_ID