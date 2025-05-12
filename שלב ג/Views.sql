-- View 1 – סיכום השכרות רכב עם פרטי הלקוח והסניף:
CREATE VIEW rental_summary AS
SELECT
  r.rentalid,
  r.startdate,
  r.enddate,
  c.model AS car_model,
  c.manufacturer,
  cu.firstname || ' ' || cu.lastname AS customer_name,
  b.branchname
FROM rental r
JOIN car c ON r.carid = c.carid
JOIN customer cu ON r.customerid = cu.customerid
JOIN branch b ON c.branchid = b.branchid;

--📌 שאילתה 1 – כל ההשכרות שבוצעו אחרי ינואר 2025
SELECT * FROM rental_summary
WHERE startdate >= '2025-01-01';

--📌 שאילתה 2 – כמה רכבים כל לקוח שכר
SELECT customer_name, COUNT(*) AS num_rentals
FROM rental_summary
GROUP BY customer_name
ORDER BY num_rentals DESC;

-- View 2 – סיכום טיולים כולל יעד, מדריך ובית מלון (מהאגף השני)
CREATE VIEW trip_overview AS
SELECT
  t.tripid,
  t.startdate,
  t.enddate,
  d.country,
  h.hotelname,
  g.guidename
FROM trip_remote t
JOIN destination_remote d ON t.zipcode = d.zipcode
JOIN hotel_remote h ON t.hotelid = h.hotelid
JOIN guide_remote g ON t.guideid = g.guideid;

-- 📌 שאילתה 1 – טיולים באירופה בלבד
SELECT * FROM trip_overview
WHERE country IN ('France', 'Germany', 'Italy', 'Spain');

-- 📌 שאילתה 2 – מספר טיולים לכל מדריך
SELECT guidename, COUNT(*) AS number_of_trips
FROM trip_overview
GROUP BY guidename
ORDER BY number_of_trips DESC;
