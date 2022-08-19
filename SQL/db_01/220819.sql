SELECT * from albums ORDER BY Title DESC LIMIT 5;
SELECT COUNT(*) AS '고객수' from customers;
SELECT COUNT(*) AS '송장수' FROM invoices WHERE BillingPostalCode != 'NULL'   ;
SELECT FirstName AS '이름' , LastName AS '성' 
FROM customers
WHERE Country = 'USA' 
ORDER BY FirstName DESC LIMIT 5;
SELECT InvoiceDate from invoices;

SELECT COUNT(*) from invoices
WHERE strftime('%Y',InvoiceDate) = '2013';

SELECT * FROM invoices 
WHERE BillingState = 'NULL'
ORDER BY InvoiceDate DESC
LIMIT 5 ;

SELECT CustomerId AS '고객ID' , 
       FirstName AS '이름' , 
       LastName AS '성'
FROM customers
WHERE FirstName like 'L%'
ORDER BY CustomerId ASC;


SELECT * FROM customers LIMIT 1;

SELECT CustomerId AS '고객ID' , 
       FirstName AS '이름' , 
       LastName AS '성'
FROM customers
WHERE FirstName like 'L%'
ORDER BY CustomerId ASC;

SELECT COUNT(*) AS '고객수' , Country AS '나라'
FROM customers
GROUP BY Country
ORDER BY COUNT(CustomerId) DESC, Country DESC
LIMIT 5;

SELECT * FROM albums LIMIT 5;

SELECT ArtistId ,COUNT(AlbumId) FROM albums 
GROUP BY ArtistId
ORDER BY COUNT(AlbumId) DESC LIMIT 1;

SELECT ArtistId ,COUNT(AlbumId) FROM albums 
GROUP BY ArtistId
HAVING COUNT(AlbumId) >= 10
ORDER BY COUNT(AlbumId) DESC;


SELECT DISTINCT State FROM customers; 


SELECT COUNT(*) AS '고객수',Country , State FROM customers 
GROUP BY Country , State
HAVING State != 'NULL'
ORDER BY COUNT(*) DESC ,Country DESC LIMIT 5;

SELECT LastName,FirstName,(-cast(strftime('%Y',BirthDate) AS INTEGER) + cast(strftime('%Y','now') AS INTEGER) + 1) AS '나이'
FROM employees
ORDER BY EmployeeId ASC;

SELECT Name from artists 
WHERE ArtistId = 
(
    SELECT 
    ArtistId from albums 
    WHERE COUNT(ArtistId) = MAX(COUNT(ArtistId))
);

SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);





SELECT 
    CustomerId ,
    CASE 
        WHEN Fax != 'NULL' THEN 'O'
        ELSE 'X'
    END AS 'Fax 유/무'
FROM customers 
ORDER BY CustomerId ASC LIMIT 5;

SELECT 
    CustomerId ,
    CASE 
        WHEN Fax != 'NULL' THEN 'O'
        ELSE 'X'
    END AS 'Fax 유/무'
FROM customers 
ORDER BY CustomerId ASC LIMIT 5;



SE