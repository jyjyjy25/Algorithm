-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME
FROM ANIMAL_INS ai JOIN ANIMAL_OUTS ao USING(ANIMAL_ID)
WHERE ai.SEX_UPON_INTAKE != ao.SEX_UPON_OUTCOME
ORDER BY ai.ANIMAL_ID