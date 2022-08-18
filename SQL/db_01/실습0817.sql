
SELECT COUNT(*) FROM healthcare;
SELECT MIN(age),MAX(age) FROM healthcare;
SELECT MAX(height),MIN(height),MAX(weight),MIN(weight) FROM healthcare;
SELECT COUNT(*) FROM healthcare WHERE 160<= height AND height <=170;
SELECT COUNT(*) FROM healthcare;
SELECT COUNT(*) FROM healthcare WHERE va_left >= 1.5 AND va_right >= 1.5 and is_drinking = 0;
SELECT COUNT(*) FROM healthcare WHERE blood_pressure <= 120; 
SELECT AVG(gender), AVG(height) FROM healthcare WHERE gender = 1;
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
SELECT id,height, weight FROM healthcare ORDER BY height LIMIT 1 OFFSET 1 ; 
SELECT COUNT(*) FROM healthcare WHERE (weight/(height*height/10000)) >= 30 AND smoking = 3;
SELECT  COUNT(*) FROM healthcare WHERE (weight/(height*height/10000)) >= 30 ;
SELECT waist FROM healthcare WHERE waist <> ''AND is_drinking = 1  ORDER BY waist DESC  LIMIT  5;


update healthcare set BMI = (weight/(height*height/10000));
SELECT id,BMI FROM healthcare ORDER BY BMI DESC LIMIT 5;
ALTER TABLE COLLUMN BMI3;
INSERT INTO healthcare  VALUES (BMI2 , weight/(height*height/10000));


ALTER TABLE healthcare ADD COLUMN BMI3 INT;
UPDATE healthcare SET BMI3 = (weight/(height*height/10000));
SELECT BMI3 from healthcare;



