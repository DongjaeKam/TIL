Select * FROM playlist_track AS 'A' ORDER BY PlaylistId DESC;
Select * FROM tracks AS 'B' ORDER BY TrackID ASC;
select TrackId FROM playlist_track limit 5;

SELECT * FROM playlist_track ;

SELECT  PlaylistId, Name FROM tracks
INNER JOIN playlist_track
ON playlist_track.TrackId = playlist_track.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;

SELECT * from tracks LIMIT 5;

SELECT * from artists LIMIT 5;

SELECT COUNT(*) FROM tracks
LEFT JOIN artists
ON tracks.Composer = artists.Name;

SELECT InvoiceLineId , InvoiceId 
FROM invoice_items
ORDER BY InvoiceId ASC LIMIT 5;


SELECT InvoiceId , CustomerId 
FROM invoices
ORDER BY InvoiceId ASC LIMIT 5;

SELECT * FROM customers limit 5;
SELECT * FROM invoices limit 5;
SELECT * FROM invoice_items limit 5;



SELECT invoices.InvoiceId , customers.CustomerId from customers 
LEFT JOIN invoices 
ON customers.CustomerId = invoices.CustomerId 
ORDER BY invoices.InvoiceId DESC LIMIT 5 ;
SELECT * from invoices LIMIT 5 ;

SELECT customers.CustomerId , COUNT(customers.CustomerId)
FROM customers
    JOIN invoices
        ON customers.CustomerId = invoices.CustomerId
    JOIN invoice_items
        ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId ASC LIMIT 5 ;









