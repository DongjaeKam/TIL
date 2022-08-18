SELECT smoking , COUNT(*) 
FROM healthcare 
WHERE smoking <> "" 
GROUP BY smoking;

SELECT is_drinking , COUNT(*) 
FROM healthcare 
WHERE is_drinking <> "" 
GROUP BY is_drinking;

SELECT is_drinking , COUNT(*) 
FROM healthcare 
WHERE is_drinking <> "" AND blood_pressure >= 200 
GROUP BY is_drinking;

SELECT is_drinking , COUNT(*) 
FROM healthcare 
WHERE is_drinking 
GROUP BY is_drinking
HAVING blood_pressure >= 200;


SELECT is_drinking , COUNT(*) 
FROM healthcare 
WHERE is_drinking <> "" AND blood_pressure >= 200 
GROUP BY is_drinking;



SELECT sido , COUNT(*) 
FROM healthcare 
GROUP BY sido
HAVING COUNT(*) >= 50000;

SELECT height , COUNT(*) 
FROM healthcare 
GROUP BY height 
ORDER BY COUNT(*) DESC
LIMIT 5;


SELECT height, weight , COUNT(*) 
FROM healthcare 
GROUP BY height , weight 
ORDER BY COUNT(*) DESC
LIMIT 5;

SELECT is_drinking, avg(waist) , COUNT(*) 
FROM healthcare 
WHERE is_drinking <> ""
GROUP BY is_drinking;

SELECT gender, avg(va_left) AS '평균 왼쪽 시력' , avg(va_right) AS '평균 오른쪽 시력' 
FROM healthcare 
GROUP BY gender;


SELECT age, avg(height) AS '평균 키' , avg(weight) AS '평균 몸무게' 
FROM healthcare 
GROUP BY age
HAVING avg(height) >= 160 AND avg(weight) >= 60;

SELECT is_drinking, smoking, avg(weight*10000/height/height) AS BMI  
FROM healthcare 
GROUP BY is_drinking , smoking
HAVING is_drinking <> "" AND smoking <> "";


SELECT is_drinking, smoking, avg(weight*10000/height/height) AS BMI  
FROM healthcare 
WHERE is_drinking <> "" AND smoking <> ""
GROUP BY is_drinking , smoking;

