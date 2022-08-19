SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMIT 5;

SELECT count(*)
from heathcare
where balance> (select avg(balance) from user);

-- 서브쿼리
-- case
