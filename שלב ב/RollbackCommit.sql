-- התחלת טרנזקציה
BEGIN;

-- דוגמה ל-ROLLBACK על טבלת Customer
UPDATE Customer
SET Phone = '0500000023'
WHERE CustomerID = 1;

-- בדיקת נתונים לאחר העדכון
SELECT * FROM Customer WHERE CustomerID = 1;

-- ביטול העדכון
ROLLBACK;

-- בדיקה שהשינוי בוטל
SELECT * FROM Customer WHERE CustomerID = 1;

-- התחלת טרנזקציה חדשה
BEGIN;

-- דוגמה ל-COMMIT על טבלת Branch
UPDATE Branch
SET Phone = '03-1111111'
WHERE BranchID = 2;

-- בדיקת נתונים לאחר העדכון
SELECT * FROM Branch WHERE BranchID = 2;

-- שמירת העדכון
COMMIT;

-- בדיקה שהשינוי נשמר
SELECT * FROM Branch WHERE BranchID = 2;
