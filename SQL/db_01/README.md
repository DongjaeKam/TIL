# 2일차 실습

  

## 사전 확인

  

### 실행

  

```bash

$ sqlite3 healthcare.sqlite3

```

  

### Column 출력 설정

  

```sql

sqlite3> .headers on

sqlite3> .mode column

```

  

### table 및 스키마 조회

  

```sql

sqlite3> .tables

healthcare

  

sqlite3> .schema healthcare

CREATE  TABLE healthcare (

id PRIMARY  KEY,

sido INTEGER  NOT  NULL,

gender INTEGER  NOT  NULL,

age INTEGER  NOT  NULL,

height INTEGER  NOT  NULL,

weight  INTEGER  NOT  NULL,

waist REAL  NOT  NULL,

va_left REAL  NOT  NULL,

va_right REAL  NOT  NULL,

  

blood_pressure INTEGER

NOT  NULL,

smoking INTEGER  NOT  NULL,

is_drinking BOOLEAN  NOT  NULL

);

```

  

## 문제

  

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

  

```sql
SELECT  COUNT(*) FROM healthcare;
```

  

```

```

  

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오.

  

```sql
SELECT MIN(age),MAX(age) FROM healthcare;
```

  

```

```

  

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

  

```sql
SELECT  MAX(height),MIN(height),MAX(weight),MIN(weight) FROM healthcare;
```

  

```

```

  

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

  

```sql
SELECT  COUNT(*) FROM healthcare WHERE  160<= height AND height <=170;
```

  

```

```

  

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.

  

```sql
SELECT waist FROM healthcare WHERE waist <> ''AND is_drinking = 1  ORDER BY waist DESC  LIMIT  5;
```

  

```

```

  

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

  

```sql
SELECT  COUNT(*) FROM healthcare WHERE va_left >= 1.5  AND va_right >= 1.5  and is_drinking = 0;
```

  

```

```

  

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

  

```sql
SELECT  COUNT(*) FROM healthcare WHERE blood_pressure <= 120;
```

  

```

```

  

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

  

```sql
SELECT  AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

  

```

```

  

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

  

```sql
SELECT  AVG(gender), AVG(height) FROM healthcare WHERE gender = 1;
```

  

```

```

  

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

  

```sql
SELECT id,height, weight  FROM healthcare ORDER BY height LIMIT  1 OFFSET 1 ;
```

  

```

```

  

### 11. BMI가 30이상인 사람의 수를 출력하시오.

  

> BMI는 체중/(키*키)의 계산 결과이다.

> 키는 미터 단위로 계산한다.

  

```sql
SELECT  COUNT(*) FROM healthcare WHERE (weight/(height*height/10000)) =;
```

  

```

```

  

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

  

> BMI는 체중/(키*키)의 계산 결과이다.

> 키는 미터 단위로 계산한다.

  

```sql
SELECT id,(weight/(height*height/10000)) FROM healthcare ORDER BY (weight/(height*height/10000)) DESC  LIMIT  5;

```

  

```

```

  

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

  

```sql

/* 마지막 문제 열추가*/

ALTER TABLE healthcare ADD COLUMN BMI INT;
UPDATE healthcare SET BMI = (weight/(height*height/10000));
SELECT id,BMI FROM healthcare ORDER BY BMI DESC  LIMIT  5;


```



```

```

  

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

  

```sql

```

  

```

```

  

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

  

```sql

```

  

```

```