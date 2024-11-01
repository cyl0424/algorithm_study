-- 코드를 작성해주세요
WITH CTE AS (
    SELECT ID, EMAIL, GROUP_CONCAT(NAME, '|', CATEGORY, '|') AS SKILL
    FROM DEVELOPERS
    JOIN SKILLCODES
    ON CODE & SKILL_CODE
    GROUP BY ID, EMAIL
)
SELECT *
FROM (SELECT CASE
        WHEN (SKILL LIKE '%Front End%' AND SKILL LIKE '%Python%') THEN 'A'
        WHEN SKILL LIKE '%C#%' THEN 'B'
        WHEN SKILL LIKE '%Front End%' THEN 'C'
        ELSE NULL
        END GRADE,
        ID, EMAIL
      FROM CTE
     ) SUB
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID