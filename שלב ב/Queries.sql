--SELECT
-- 1. רשימת רכבים שהושכרו בין תאריכים מסוימים כולל פרטי לקוח ורכב
SELECT c.FirstName, c.LastName, car.Model, car.Manufacturer, r.StartDate, r.EndDate
FROM Rental r
JOIN Customer c ON r.CustomerID = c.CustomerID
JOIN Car car ON r.CarID = car.CarID
WHERE r.StartDate >= '2025-01-01' AND r.EndDate <= '2025-12-31';

-- 2. חודשים שבהם מספר ההשכרות היה מעל הממוצע החודשי
SELECT EXTRACT(YEAR FROM StartDate) AS Year,
       EXTRACT(MONTH FROM StartDate) AS Month,
       COUNT(*) AS TotalRentals
FROM Rental
GROUP BY Year, Month
HAVING COUNT(*) > (
    SELECT AVG(MonthlyCount) FROM (
        SELECT COUNT(*) AS MonthlyCount
        FROM Rental
        GROUP BY EXTRACT(YEAR FROM StartDate), EXTRACT(MONTH FROM StartDate)
    ) AS MonthlyData
)
ORDER BY Year, Month;

-- 3. רכבים שהושכרו בסכום גבוה יותר מהממוצע של אותו רכב
--SELECT RentalID, TotalCost, CarID
--FROM Rental r1
--WHERE TotalCost > (
--    SELECT AVG(r2.TotalCost)
--    FROM Rental r2
--    WHERE r2.CarID = r1.CarID
--)
--ORDER BY CarID;

-- 3 ממוצע מספר מושבים לרכבים שהושכרו
SELECT AVG(car.NumSeats) AS AvgSeats
FROM Rental r
JOIN Car car ON r.CarID = car.CarID;

-- 4. רכבים שלא עברו תחזוקה כלל
SELECT car.CarID, car.Model
FROM Car car
LEFT JOIN Maintenance m ON car.CarID = m.CarID
WHERE m.MaintenanceID IS NULL;

-- 5. תשלום אחרון שבוצע לכל לקוח (לפי תאריך)
SELECT DISTINCT ON (r.CustomerID) r.CustomerID, c.FirstName, c.LastName, p.PaymentDate, p.Amount
FROM Rental r
JOIN Customer c ON r.CustomerID = c.CustomerID
JOIN Payment p ON r.PaymentID = p.PaymentID
ORDER BY r.CustomerID, p.PaymentDate DESC;

-- 6. תאריכי התחלה של השכרות בחודש מרץ בלבד
SELECT RentalID, StartDate
FROM Rental
WHERE EXTRACT(MONTH FROM StartDate) = 3;

-- 7. רכבים עם ההכנסה הכוללת שלהם – רק כאלה שהרוויחו מעל הממוצע
SELECT car.CarID, car.Model, SUM(r.TotalCost) AS TotalIncome
FROM Car car
JOIN Rental r ON car.CarID = r.CarID
GROUP BY car.CarID, car.Model
HAVING SUM(r.TotalCost) > (
    SELECT AVG(TotalCost) FROM Rental
)
ORDER BY TotalIncome DESC;

-- 8. ממוצע התשלום לפי אמצעי תשלום – רק אם קיימים תשלומים מעל 500 באותו אמצעי
SELECT PaymentMethod, ROUND(AVG(Amount), 2) AS AvgAmount
FROM Payment
WHERE PaymentMethod IN (
    SELECT DISTINCT PaymentMethod FROM Payment WHERE Amount > 500
)
GROUP BY PaymentMethod;

-- 9. לקוחות שהגיל שלהם גבוה מהממוצע הכללי
SELECT FirstName, LastName, DateOfBirth,
       EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) AS Age
FROM Customer
WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) > (
    SELECT AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth))) FROM Customer
)
ORDER BY Age DESC;


-- 10. סך התשלומים לפי רכב בסניפים מהדרום בלבד
SELECT car.CarID, car.Model, SUM(p.Amount) AS TotalPayments
FROM Car car
JOIN Rental r ON car.CarID = r.CarID
JOIN Payment p ON r.PaymentID = p.PaymentID
WHERE car.BranchID IN (
    SELECT BranchID
    FROM Branch
    WHERE Location IN (
        SELECT Location FROM Branch WHERE Location ILIKE '%south%'
    )
)
GROUP BY car.CarID, car.Model
ORDER BY TotalPayments DESC;


-- 11. לקוחות שביצעו השכרות לרכבים מסניפים באזור המרכז או הצפון
SELECT DISTINCT c.CustomerID, c.FirstName, c.LastName
FROM Customer c
JOIN Rental r ON c.CustomerID = r.CustomerID
JOIN Car car ON r.CarID = car.CarID
WHERE car.BranchID IN (
    SELECT BranchID
    FROM Branch
    WHERE Location ILIKE '%center%' OR Location ILIKE '%north%'
);


-- 12. תשלומים שבוצעו באמצעים שהיו פעילים רק בחודשים בהם בוצעו יותר מ-20 השכרות
SELECT PaymentID, PaymentMethod, PaymentDate, Amount
FROM Payment
WHERE EXTRACT(MONTH FROM PaymentDate) IN (
    SELECT EXTRACT(MONTH FROM StartDate)
    FROM Rental
    GROUP BY EXTRACT(MONTH FROM StartDate)
    HAVING COUNT(*) > 20
)
ORDER BY PaymentDate;

-- 13. לקוחות שמבוגרים מגיל 70 ושלא ביצעו אף השכרה במהלך השנה הנוכחית (2025)
SELECT c.CustomerID, c.FirstName, c.LastName, c.Email, c.Phone, c.DateOfBirth
FROM Customer c
WHERE 
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.DateOfBirth)) > 70
    AND c.CustomerID NOT IN (
        SELECT r.CustomerID
        FROM Rental r
        WHERE EXTRACT(YEAR FROM r.StartDate) = EXTRACT(YEAR FROM CURRENT_DATE)
    );

--DELETE
--1. מחיקת רכבים שהמחיר היומי שלהם נמוך מהמינימום של ממוצע העלות להשכרה
DELETE FROM Car
WHERE PricePerDay < (
    SELECT MIN(AvgDailyCost)
    FROM (
        SELECT CarID, AVG(TotalCost / GREATEST(DATE_PART('day', EndDate - StartDate), 1)) AS AvgDailyCost
        FROM Rental
        GROUP BY CarID
    ) AS CarAverages
);

--2. מחיקת רשומות תחזוקה לרכבים שנמצאים בסניפים עם הכי מעט רכבים
DELETE FROM Maintenance
WHERE CarID IN (
    SELECT CarID
    FROM Car
    WHERE BranchID IN (
        SELECT BranchID
        FROM Car
        GROUP BY BranchID
        HAVING COUNT(*) = (
            SELECT MIN(CarCount)
            FROM (
                SELECT COUNT(*) AS CarCount
                FROM Car
                GROUP BY BranchID
            ) AS SubCounts
        )
    )
);

--3. מחיקת תחזוקה לרכבים שההכנסה השנתית הממוצעת שלהם נמוכה מהממוצע של כל הרכבים 
DELETE FROM Maintenance
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    GROUP BY CarID
    HAVING AVG(TotalCost) < (
        SELECT AVG(TotalCost)
        FROM Rental
    )
);

--4. מחיקה מתשלומים את אלו שלא ביצעו אף השכרה ושבוצעו במועדים חריגים
DELETE FROM Payment
WHERE PaymentID NOT IN (
    SELECT DISTINCT PaymentID
    FROM Rental
)
AND PaymentID IN (
    SELECT PaymentID
    FROM Payment
    WHERE EXTRACT(DOW FROM PaymentDate) IN (0, 6)  -- בוצעו בשישי או שבת
    AND Amount < (
        SELECT AVG(Amount)
        FROM Payment
    )
);


--UPDATE
--1. עדכון סטטוס רכב ל־"Available" אם תאריך סיום ההשכרה עבר
UPDATE Car
SET Status = 'Available'
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    WHERE EndDate < CURRENT_DATE
);

--2. העלאת מחיר ליום ב־15% לרכבים ששכרו אותם יותר מ־5 פעמים
UPDATE Car
SET PricePerDay = PricePerDay * 1.15
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    GROUP BY CarID
    HAVING COUNT(*) > 5
);

--3. עדכון מחיר יומי של רכבים מושכרים הכי הרבה פעמים
UPDATE Car
SET PricePerDay = PricePerDay * 1.2
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    GROUP BY CarID
    HAVING COUNT(*) = (
        SELECT MAX(RentalCount)
        FROM (
            SELECT CarID, COUNT(*) AS RentalCount
            FROM Rental
            GROUP BY CarID
        ) AS RentalCounts
    )
);

--4. UPDATE – סימון השכרות הכי יקרות בכל שנה (הוספת תשלום סמלי נוסף)
UPDATE Rental
SET TotalCost = TotalCost + 100
WHERE TotalCost IN (
    SELECT MAX(TotalCost)
    FROM Rental
    GROUP BY EXTRACT(YEAR FROM StartDate)
);

--5. UPDATE – שינוי אימיילים של לקוחות שביצעו הכי הרבה תשלומים
UPDATE Customer
SET Email = CONCAT('vip_', Email)
WHERE CustomerID IN (
    SELECT r.CustomerID
    FROM Rental r
    JOIN Payment p ON r.PaymentID = p.PaymentID
    GROUP BY r.CustomerID
    HAVING COUNT(p.PaymentID) = (
        SELECT MAX(PaymentCount)
        FROM (
            SELECT r.CustomerID, COUNT(p.PaymentID) AS PaymentCount
            FROM Rental r
            JOIN Payment p ON r.PaymentID = p.PaymentID
            GROUP BY r.CustomerID
        ) AS CustomerPayments
    )
);

--6. הUPDATE – עדכון טלפונים של סניפים שעם הכי הרבה רכבים
UPDATE Branch
SET Phone = '03-9999999'
WHERE BranchID IN (
    SELECT BranchID
    FROM Car
    GROUP BY BranchID
    HAVING COUNT(*) = (
        SELECT MAX(CarCount)
        FROM (
            SELECT BranchID, COUNT(*) AS CarCount
            FROM Car
            GROUP BY BranchID
        ) AS CountPerBranch
    )
);
