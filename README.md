# DBProject_4254_2894

# Trips

# Rental car 

## Shira Shenfel 326444254
## Itti Chaimson 326282894

## Table of Contents  
- [Phase 1: Design and Build the Database](#phase-1-design-and-build-the-database)  
  - [Introduction](#introduction)  
  - [ERD (Entity-Relationship Diagram)](#erd-entity-relationship-diagram)  
  - [DSD (Data Structure Diagram)](#dsd-data-structure-diagram)  
  - [ERD Pgadmin](#erd-pgadmin)
  - [Design Decisions](#design-decisions)
  - [SQL Scripts](#sql-scripts)  
  - [Data](#data)
    - [First tool](#first-tool-using-csv-file)

       -[Branch Table Data Entry](#branch-table-data-entry)

       -[Payments Table Data Entry](#payments-table-data-entry)
    - [Second tool](#second-tool-using-generatedata-to-create-csv-file)

       -[Payments Table Data Entry](#payments-table-data-entry-1)
    - [Third tool](#third-tool-using-mockaro-to-create-csv-file)

       -[Car Table Data Entry](#car-table-data-entry)
    - [Fourth tool](#fourth-tool-using-python-to-generate-a-csv-file-and-insert-it-into-the-database)

       -[Customers Table Data Entry](#customers-table-data-entry)

       -[Rental Table Data Entry](#rental-table-data-entry)
       
       -[Maintenance Table Data Entry](#maintenance-table-data-entry)
  - [Backup](#backup)
  - [Data Restoration](#data-restoration)  
- [Phase 2: Queries and Constraints](#phase-2-queries-and-constraints) 
  - [Queries](#queries)
    - [SELECT](#select)
    - [DELETE](#delete)
    - [UPDATE](#update)
  - [Constraints](#constraints)
  - [Backup2](#backup2)  

## Phase 1: Design and Build the Database  

### Introduction

The **car rental system** is one of the core components of the **“Trips”** project.
Its goal is to enable smart, organized, and automated management of processes such as rentals, maintenance, payments, and branches for customers.

The system is designed for organizations that provide car rental services to customers on an ongoing basis.
It allows the storage, analysis, and management of all the information required for the efficient operation of a rental system.
The data is stored in a relational database that maintains logical relationships between entities, based on normalization rules and clear separation of responsibilities across tables.

#### 🧩 Main Data Structure in the System:
🔹 **Customers (Customer)** – Stores personal information of customers: first and last name, phone number, email address, driver’s license number, and date of birth.
Each customer is uniquely identified by CustomerID, and the system tracks all rentals made by the customer.

🔹 **Cars (Car)** – The system manages full data on the vehicle fleet: manufacturer, model, year of production, daily rental price, number of seats, status (Available / Rented / In Maintenance), and a unique license plate.
Each car is assigned to a branch and its status can change over time.

🔹 **Branches (Branch)** – Management of the company's active branches, including branch name, full address, and contact details.
Cars are physically assigned to these branches and serve as pick-up and return locations for rentals.

🔹 **Rentals (Rental)** – The system's core activity. Each rental includes a start and end date, calculated total cost, and is linked to a specific customer, car, and payment.
Each car and customer can only be active in one rental at a time (according to system constraints).

🔹 **Payments (Payment)** – Every rental requires a payment. The system records the amount, payment method (credit card, cash, PayPal), and date of payment.
The data is linked to the corresponding rental record.

🔹 **Maintenance (Maintenance)** – The system documents maintenance actions, recurring issues, and preventive treatments.
It records the description, cost, date, and the car associated with the maintenance.
This enables historical tracking and future maintenance planning.  

#### ⚙️ Core Functionality:
--Create car rentals for customers over a defined date range

--Automatically calculate the total cost based on rental days and car’s daily price

--Monitor car status (Available / Rented / In Maintenance)

--Manage payments for each rental with support for various payment methods

--Maintain vehicle maintenance history and reassign cars to branches as needed

--Maintain logical links between entities: each car belongs to a branch, and each rental links to a customer, car, and payment

--Import data from external sources (CSV / external tools / scripts) and generate reports 

#### 🎯 System Objectives:
• Reduce manual errors

• Improve processing time for rentals

• Monitor and manage vehicle inventory

• Enable flexibility in adding branches, cars, and customers

###  ERD (Entity-Relationship Diagram)    
![ERD Diagram](ERD.png)

###  DSD (Data Structure Diagram)   
![DSD Diagram](DSD.png)  

### ERD Pgadmin
![ERD - PG](ERDPG.png)

### Design Decisions
#### 🧱 Entities & Attributes
**• Customer**
Represents registered customers in the system.

`CustomerID` – Unique identifier

`FirstName` – First name

`LastName` – Last name

`Phone` – Contact number

`Email` – Email address

`LicenseNumber` – Unique driving license number

`DateOfBirth` – Date of birth (type: `DATE`)

**• Car**
Represents cars available for rental.

`CarID` – Unique identifier

`LicensePlate` – Unique license plate

`Model` – Car model

`Manufacturer` – Manufacturer

`Year` – Year of manufacture

`Status` – Status (Available / Rented / In Maintenance)

`PricePerDay` – Rental cost per day

`BranchID` – Foreign key referring to the Branch

`NumSeats` – Number of seats in the car

**• Rental**
Describes rental transactions.

`RentalID` – Unique identifier

`CustomerID`– Foreign key to Customer

`CarID` – Foreign key to Car

`StartDate` – Rental start date (`DATE`)

`EndDate` – Rental end date (`DATE`)

`TotalCost` – Calculated field based on duration and price

`PaymentID` – Foreign key to Payment

**• Payment**
`Tracks payments for rentals.

`PaymentID` – Unique identifier

`RentalID` – Foreign key to Rental

`PaymentDate` – Payment date (`DATE`)

`Amount` – Payment amount

`PaymentMethod` – e.g., Credit Card, Cash, PayPal

**• Branch**
Represents company branches where cars are located.

`BranchID` – Unique identifier

`BranchName` – Name of the branch

`Location` – Branch address

`Phone` – Contact number

**• Maintenance**
Records car maintenance history.

`MaintenanceID` – Unique identifier

`CarID` – Foreign key to Car

`MaintenanceDate` – Date of maintenance (`DATE`)

`Description` – Fault or service description

`Cost` – Maintenance cost

#### 🔗 Relationships
**Customer Rents** – One-to-many (`1:M`) between Customer and Rental
→ A customer can have multiple rentals, but each rental belongs to one customer.

**Car is Rented** – One-to-many (`1:M`) between Car and Rental
→ A car can be rented multiple times, but each rental refers to one car.

**Rental Includes Payment** – One-to-one (`1:1`) between Rental and Payment
→ Each rental has exactly one payment record, and each payment is linked to one rental.

**Car is Managed By Branch**– One-to-many (`1:M`) between Branch and Car
→ A branch manages multiple cars, but each car belongs to one branch only.

**Car Undergoes Maintenance** – One-to-many (`1:M`) between Car and Maintenance
→ A car can undergo multiple maintenance records, but each maintenance belongs to one car.

#### 🧠 Design Considerations
Use of **foreign keys (`FK`)** to ensure data consistency

**Normalization** – Each entity stands alone, with no data redundancy

Use of **`unique` constraints** for fields like `LicensePlate` and `LicenseNumber`

Enorced **1:1 relationship** between `Rental` and `Payment` to ensure that every rental has a single associated payment

Structured according to **Third Normal Form (3NF)** for optimal performance and no duplication

###  SQL Scripts  
Provide the following SQL scripts:  
- **Create Tables Script** - The SQL script for creating the database tables is available in the repository:  

📜 **[View `create1.sql`](שלב%20א/creata1.sql)**  

- **Insert Data Script** - The SQL script for insert data to the database tables is available in the repository:  

📜 **[View `insertTables.sql`](שלב%20א/insertTables.sql)**  
 
- **Drop Tables Script** - The SQL script for droping all tables is available in the repository:  

📜 **[View `dropTables.sql`](שלב%20א/dropTables.sql)**  

- **Select All Data Script**  - The SQL script for selectAll tables is available in the repository:  

📜 **[View `selectAll.sql`](שלב%20א/selectAll.sql)**  
  
###  Data  
####  First tool: using csv file
##### Branch Table Data Entry:
• Branch ID: 4–403
📜**[View `branches1.csv`](שלב%20א/DataImportFiles/branches1.csv)**

![image1](שלב%20א/DataImportFiles/image.png)

![image2](שלב%20א/DataImportFiles/image-1.png)

results for  the command `SELECT 'Branch' AS TableName, COUNT(*) FROM Branch;`:
![image3](שלב%20א/DataImportFiles/image-2.png) 

##### Payments Table Data Entry:
• Payment ID: 4–23
📜**[View `payments2.csv`](שלב%20א/DataImportFiles/payments2.csv)**

![image4](שלב%20א/DataImportFiles/image-3.png)

![image5](שלב%20א/DataImportFiles/image-4.png)
#### Second tool: using [generatedata](https://generatedata.com/generator). to create csv file
##### Payments Table Data Entry:
• Payment ID: 24-396
📜**[View `PaymentsInsert1.csv`](שלב%20א/generatedataFiles/PaymentsInsert1.csv)**

![image6](שלב%20א/generatedataFiles/image-5.png)

![image7](שלב%20א/generatedataFiles/image-6.png)

![image8](שלב%20א/generatedataFiles/image-7.png)

results for  the command `SELECT 'Payment' AS TableName, COUNT(*) FROM Payment;`:
![image9](שלב%20א/generatedataFiles/image-8.png)

####  Third tool: using [mockaro](https://www.mockaroo.com/) to create csv file
##### Car Table Data Entry:
• Car ID: 4–403
-  Formula of Car ID: `this + 4`
📜 **[View `mock_car.csv`](שלב%20א/mockarooFiles/mock_car.csv)**

![image10](שלב%20א/mockarooFiles/image-9.png)

![image11](שלב%20א/mockarooFiles/image-10.png)

![alt text](שלב%20א/mockarooFiles/תמונה%20של%20WhatsApp‏%202025-03-29%20בשעה%2023.01.14_eb709eab.jpg)

results for  the command `SELECT 'Car' AS TableName, COUNT(*) FROM Car;`:
![image12](שלב%20א/mockarooFiles/image-11.png)

####  Fourth Tool: Using Python to generate a CSV file and insert it into the database
##### Customers Table Data Entry:
• Customer ID: 4–403
📜 **[View `customers.csv`](שלב%20א/Programing1/customers.csv)**

**[View `CustomersInsert.py`](שלב%20א/Programing1/CustomerInsert.py)**

![image13](שלב%20א/Programing1/image-12.png)

results for  the command `SELECT 'Customer' AS TableName, COUNT(*) FROM Customer;`:
![image14](שלב%20א/Programing1/image-13.png)

##### Rental Table Data Entry:
• Rental ID: 4–403
📜 **[View `rentals.csv`](שלב%20א/Programing1/rentals.csv)**

**[View `RentalInsert.py`](שלב%20א/Programing1/RentalInsert.py)**

![alt1 text](שלב%20א/Programing1/תמונה%20של%20WhatsApp‏%202025-03-29%20בשעה%2023.58.27_06a936d2.jpg)

![image15](שלב%20א/Programing1/image-14.png)

results for  the command `SELECT 'Rental' AS TableName, COUNT(*) FROM Rental;`:
![image16](שלב%20א/Programing1/image-15.png)

##### Maintenance Table Data Entry:
• Maintenance ID: 4–403
📜 **[View `maintenance.csv`](שלב%20א/Programing1/maintenance.csv)**

**[View `MaintenanceInsert.py`](שלב%20א/Programing1/MaintenancesInsert.py)**

![alt3 text](שלב%20א/Programing1/תמונה%20של%20WhatsApp‏%202025-03-29%20בשעה%2023.59.18_245283a0.jpg)

![image17](שלב%20א/Programing1/image-16.png)

results for  the command `SELECT 'Maintenance' AS TableName, COUNT(*) FROM Maintenance;`:
![image18](שלב%20א/Programing1/image-17.png)
### Backup 
-   backups files are kept with the date and hour of the backup:  

[Navigate to the backups folder](שלב%20א/BackupFiles/Backup2.backup)

[Also backups folder](שלב%20א/BackupFiles/Backup.sql)

![image19](שלב%20א/BackupFiles/image-18.png)

### Data Restoration

![image20](שלב%20א/BackupFiles/image-19.png)


## Phase 2: Queries and Constraints

### Queries

#### SELECT
##### 1. רשימת רכבים שהושכרו בין תאריכים מסוימים כולל פרטי לקוח ורכב

SELECT c.FirstName, c.LastName, car.Model, car.Manufacturer, r.StartDate, r.EndDate
FROM Rental r
JOIN Customer c ON r.CustomerID = c.CustomerID
JOIN Car car ON r.CarID = car.CarID
WHERE r.StartDate >= '2025-01-01' AND r.EndDate <= '2025-12-31';


שאילתה זו מציגה את פרטי ההשכרות שבוצעו בשנת 2025 בלבד. היא מצטרפת בין טבלאות הלקוח (`Customer`) והרכב (`Car`) דרך טבלת ההשכרות (`Rental`) כדי להחזיר את שם הלקוח, דגם הרכב, היצרן, ותאריכי ההשכרה. מטרת השאילתה היא להבין איזה לקוחות שכרו רכבים באותה שנה ואילו רכבים היו פופולריים.

![Select1](שלב%20ב/PicturesSELECT/Select1.png)

##### 2. חודשים שבהם מספר ההשכרות היה מעל הממוצע החודשי
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


השאילתה מחשבת את מספר ההשכרות עבור כל חודש (שנה + חודש), ואז באמצעות תת־שאילתה פנימית מחשבת את הממוצע החודשי לכלל התקופה. היא מחזירה רק את החודשים שהיו פעילים יותר מהממוצע. זוהי שאילתה עסקית שימושית לניתוח עומסים עונתיים.

![Select2](שלב%20ב/PicturesSELECT/Select2.png)

##### 3 ממוצע מספר מושבים לרכבים שהושכרו
SELECT AVG(car.NumSeats) AS AvgSeats
FROM Rental r
JOIN Car car ON r.CarID = car.CarID;


מטרת השאילתה לחשב את מספר המושבים הממוצע של רכבים שבאמת הושכרו. היא עושה שימוש ב־JOIN בין Rental ו־Car, כך שהממוצע מחושב רק על רכבים פעילים במערכת. תוצאה זו יכולה לשמש ככלי תכנוני לרכישת רכבים עם קיבולת מתאימה לביקוש.

![Select3](שלב%20ב/PicturesSELECT/Select3.png)

##### 4. רכבים שלא עברו תחזוקה כלל
SELECT car.CarID, car.Model
FROM Car car
LEFT JOIN Maintenance m ON car.CarID = m.CarID
WHERE m.MaintenanceID IS NULL;


שאילתה זו עושה שימוש ב־LEFT JOIN כדי להחזיר את כל הרכבים שבמערכת, ומסננת מתוכם את אלו שאין להם התאמה בטבלת Maintenance. זוהי דרך לאתר רכבים שלא עברו שום טיפול תחזוקתי – מידע חשוב למניעת תקלות.

![Select4](שלב%20ב/PicturesSELECT/Select4.png)

##### 5. תשלום אחרון שבוצע לכל לקוח (לפי תאריך)
SELECT DISTINCT ON (r.CustomerID) r.CustomerID, c.FirstName, c.LastName, p.PaymentDate, p.Amount
FROM Rental r
JOIN Customer c ON r.CustomerID = c.CustomerID
JOIN Payment p ON r.PaymentID = p.PaymentID
ORDER BY r.CustomerID, p.PaymentDate DESC;


באמצעות DISTINCT ON – השאילתה שולפת את שורת התשלום האחרונה (לפי תאריך) של כל לקוח. היא מחזירה את שם הלקוח, הסכום ותאריך התשלום האחרון. זו שאילתה חיונית לצורכי שירות לקוחות ובדיקות פיננסיות.

![Select5](שלב%20ב/PicturesSELECT/Select5.png)

##### 6. תאריכי התחלה של השכרות בחודש מרץ בלבד
SELECT RentalID, StartDate
FROM Rental
WHERE EXTRACT(MONTH FROM StartDate) = 3;


שאילתה פשוטה יותר המבודדת את ההשכרות שבוצעו בחודש מרץ, על ידי פילוח לפי חודש מתוך שדה התאריך. שימושי לבחינת עונתיות של ההשכרות בתחילת האביב.

![Select6](שלב%20ב/PicturesSELECT/Select6.png)

##### 7. רכבים עם ההכנסה הכוללת שלהם – רק כאלה שהרוויחו מעל הממוצע
SELECT car.CarID, car.Model, SUM(r.TotalCost) AS TotalIncome
FROM Car car
JOIN Rental r ON car.CarID = r.CarID
GROUP BY car.CarID, car.Model
HAVING SUM(r.TotalCost) > (
    SELECT AVG(TotalCost) FROM Rental
)
ORDER BY TotalIncome DESC;


השאילתה מצטרפת את טבלאות Car ו־Rental, מסכמת את ההכנסה לכל רכב, ומשווה אותה לממוצע הכללי של כלל הרכבים. היא מחזירה רק את הרכבים הרווחיים ביותר, דבר המסייע לקבלת החלטות עסקיות.

![Select7](שלב%20ב/PicturesSELECT/Select7.png)

##### 8. ממוצע התשלום לפי אמצעי תשלום – רק אם קיימים תשלומים מעל 500 באותו אמצעי
SELECT PaymentMethod, ROUND(AVG(Amount), 2) AS AvgAmount
FROM Payment
WHERE PaymentMethod IN (
    SELECT DISTINCT PaymentMethod FROM Payment WHERE Amount > 500
)
GROUP BY PaymentMethod;


שאילתה זו משתמשת בתנאי פנימי שמחזיר רק אמצעי תשלום שבהם היה לפחות תשלום אחד מעל 500 ש"ח, ואז מחשבת ממוצע רק עבורם. כך ניתן לבדוק אילו אמצעים משמשים לעסקאות משמעותיות יותר.

![Select8](שלב%20ב/PicturesSELECT/Select8.png)

##### 9. לקוחות שהגיל שלהם גבוה מהממוצע הכללי
SELECT FirstName, LastName, DateOfBirth,
       EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) AS Age
FROM Customer
WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) > (
    SELECT AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth))) FROM Customer
)
ORDER BY Age DESC;


השאילתה מחשבת את גיל כל לקוח מתוך תאריך הלידה, ומשווה לממוצע הגילאים. היא מחזירה רק את הלקוחות שמבוגרים יותר מהממוצע הכללי – כלי טוב לבחינת קהל היעד.

![Select9](שלב%20ב/PicturesSELECT/Select9.png)

##### 10. סך התשלומים לפי רכב בסניפים מהדרום בלבד
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


באמצעות מסננים על מיקומי סניפים שמכילים את המילה "south", השאילתה בודקת את סך כל התשלומים לפי כל רכב. מאפשר ניתוח ביצועים של אזור גאוגרפי מסוים.

![Select10](שלב%20ב/PicturesSELECT/Select10.png)

##### 11. לקוחות שביצעו השכרות לרכבים מסניפים באזור המרכז או הצפון
SELECT DISTINCT c.CustomerID, c.FirstName, c.LastName
FROM Customer c
JOIN Rental r ON c.CustomerID = r.CustomerID
JOIN Car car ON r.CarID = car.CarID
WHERE car.BranchID IN (
    SELECT BranchID
    FROM Branch
    WHERE Location ILIKE '%center%' OR Location ILIKE '%north%'
);


שאילתה זו מחזירה לקוחות שביצעו השכרות מרכבים השייכים לסניפים שמיקומם כולל את המילים "center" או "north". מאפשר להבין מי הלקוחות שפעילים באזורים מסוימים בארץ.

![Select11](שלב%20ב/PicturesSELECT/Select11.png)

##### 12. תשלומים שבוצעו באמצעים שהיו פעילים רק בחודשים בהם בוצעו יותר מ-20 השכרות
SELECT PaymentID, PaymentMethod, PaymentDate, Amount
FROM Payment
WHERE EXTRACT(MONTH FROM PaymentDate) IN (
    SELECT EXTRACT(MONTH FROM StartDate)
    FROM Rental
    GROUP BY EXTRACT(MONTH FROM StartDate)
    HAVING COUNT(*) > 20
)
ORDER BY PaymentDate;


מחזירה את כל התשלומים שבוצעו באותם חודשים שבהם מספר ההשכרות היה מעל 20 – לצורך בדיקת פעילות כספית בתקופות עומס.

![Select12](שלב%20ב/PicturesSELECT/Select12.png)

##### 13. לקוחות שמבוגרים מגיל 70 ושלא ביצעו אף השכרה במהלך השנה הנוכחית (2025)
SELECT c.CustomerID, c.FirstName, c.LastName, c.Email, c.Phone, c.DateOfBirth
FROM Customer c
WHERE 
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, c.DateOfBirth)) > 70
    AND c.CustomerID NOT IN (
        SELECT r.CustomerID
        FROM Rental r
        WHERE EXTRACT(YEAR FROM r.StartDate) = EXTRACT(YEAR FROM CURRENT_DATE)
    );


מאתרת לקוחות מבוגרים (מעל גיל 70) שלא ביצעו כלל השכרה במהלך שנת 2025. המידע הזה חשוב כדי לעקוב אחר קהלים לא פעילים.

![Select13](שלב%20ב/PicturesSELECT/Select13.png)

#### DELETE
##### 1. מחיקת רכבים שהמחיר היומי שלהם נמוך מהמינימום של ממוצע העלות להשכרה

DELETE FROM Car
WHERE PricePerDay < (
    SELECT MIN(AvgDailyCost)
    FROM (
        SELECT CarID, AVG(TotalCost / GREATEST(DATE_PART('day', EndDate - StartDate), 1)) AS AvgDailyCost
        FROM Rental
        GROUP BY CarID
    ) AS CarAverages
);


שאילתה זו מחשבת עבור כל רכב את ממוצע עלות ההשכרה ליום (סכום חלקי מספר ימי ההשכרה), ואז בודקת את המינימום מתוך הממוצעים. לבסוף, נמחקים הרכבים שמחירם היומי נמוך מערך זה. זוהי פעולה עסקית חשובה לסילוק רכבים לא רווחיים מהמלאי.

###### Before:
![Delete1_before](שלב%20ב/PicturesDELETE/Delete1_before.png)

###### Run:
![Delete1](שלב%20ב/PicturesDELETE/Delete1.png)

###### After:
![Delete1_after](שלב%20ב/PicturesDELETE/Delete1_after.png)

##### 2. מחיקת רשומות תחזוקה לרכבים שנמצאים בסניפים עם הכי מעט רכבים
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


באמצעות שאילתות מקוננות, מזוהות תחזוקות ששייכות לרכבים שנמצאים בסניפים עם מספר הרכבים הנמוך ביותר. מטרת הפעולה היא לנקות נתונים פחות רלוונטיים או לא חיוניים.

###### Before:
![Delete23_before](שלב%20ב/PicturesDELETE/Delete23_before.png)

###### Run:
![Delete2](שלב%20ב/PicturesDELETE/Delete2.png)

###### After:
![Delete2_after](שלב%20ב/PicturesDELETE/Delete2_after.png)

#### 3. מחיקת תחזוקה לרכבים שההכנסה השנתית הממוצעת שלהם נמוכה מהממוצע של כל הרכבים 
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


מזוהות תחזוקות שמיוחסות לרכבים בעלי הכנסה שנתית ממוצעת נמוכה מהממוצע הכללי. מחיקה זו מסייעת להתמקד רק ברכבים משתלמים לצורך תחזוקה עתידית.

###### Before:
![Delete23_before](שלב%20ב/PicturesDELETE/Delete23_before.png)

###### Run:
![Delete3](שלב%20ב/PicturesDELETE/Delete3.png)

###### After:
![Delete3_after](שלב%20ב/PicturesDELETE/Delete3_after.png)

##### 4. מחיקה מתשלומים את אלו שלא ביצעו אף השכרה ושבוצעו במועדים חריגים
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


השאילתה מוחקת תשלומים חשודים שלא קושרו לשום השכרה (NOT IN) וגם בוצעו בסוף השבוע (שישי/שבת) ובסכום נמוך מהממוצע. מסייעת לשמירה על תקינות והיגיון בנתונים הפיננסיים.

###### Before:
![Delete4_before](שלב%20ב/PicturesDELETE/Delete4_bafore.png)

###### Run:
![Delete4](שלב%20ב/PicturesDELETE/Delete4.png)

###### After:
![Delete4_after](שלב%20ב/PicturesDELETE/Delete4_after.png)


#### UPDATE
##### 1. עדכון סטטוס רכב ל־"Available" אם תאריך סיום ההשכרה עבר
UPDATE Car
SET Status = 'Available'
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    WHERE EndDate < CURRENT_DATE
);


השאילתה בודקת אילו רכבים הסתיימה ההשכרה שלהם (כלומר תאריך הסיום קטן מהתאריך הנוכחי), ומעדכנת את הסטטוס שלהם ל־"Available".
זה שומר על עדכניות המידע בטבלת הרכבים, כך שהמערכת תדע אילו רכבים באמת זמינים להשכרה כרגע. זה חשוב כדי לא להחסיר רכבים מזמינות למרות שכבר חזרו.

###### Before:
![Update123_before](שלב%20ב/PicturesUPDATE/Update123_before.png)

###### Run:
![Update1](שלב%20ב/PicturesUPDATE/Update1.png)

###### After:
![Update1_after](שלב%20ב/PicturesUPDATE/Update1_after.png)

##### 2. העלאת מחיר ליום ב־15% לרכבים ששכרו אותם יותר מ־5 פעמים
UPDATE Car
SET PricePerDay = PricePerDay * 1.15
WHERE CarID IN (
    SELECT CarID
    FROM Rental
    GROUP BY CarID
    HAVING COUNT(*) > 5
);


השאילתה מחשבת אילו רכבים שימשו ליותר מ־5 השכרות, ומעלה את המחיר היומי שלהם ב־15%.
הרעיון כאן הוא לנצל רכבים פופולריים כדי למקסם רווחים. רכבים שמבוקשים יותר יכולים לשאת מחיר גבוה יותר – בדומה לדינמיקת תמחור של חברות השכרה אמיתיות.

###### Before:
![Update123_before](שלב%20ב/PicturesUPDATE/Update123_before.png)

###### Run:
![Update2](שלב%20ב/PicturesUPDATE/Update2.png)

###### After:
![Update2_after](שלב%20ב/PicturesUPDATE/Update2_after.png)

##### 3. עדכון מחיר יומי של רכבים מושכרים הכי הרבה פעמים
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


המערכת מזהה את הרכב שהושכר הכי הרבה פעמים מכלל הרכבים – ומעלה את המחיר היומי שלו ב־20%.
זה מבטא מודל תמחור מבוסס ביקוש. כאשר רכב פופולרי במיוחד, הוא יכול להיות מתומחר גבוה יותר, וכך למקסם רווחיות מבלי לפגוע בביקוש.

###### Before:
![Update123_before](שלב%20ב/PicturesUPDATE/Update123_before.png)

###### Run:
![Update3](שלב%20ב/PicturesUPDATE/Update3.png)

###### After:
![Update3_after](שלב%20ב/PicturesUPDATE/Update3_after.png)

##### 4. UPDATE – סימון השכרות הכי יקרות בכל שנה (הוספת תשלום סמלי נוסף)
UPDATE Rental
SET TotalCost = TotalCost + 100
WHERE TotalCost IN (
    SELECT MAX(TotalCost)
    FROM Rental
    GROUP BY EXTRACT(YEAR FROM StartDate)
);


השאילתה מאתרת את ההשכרה היקרה ביותר בכל שנה לפי TotalCost, ומוסיפה 100 ש"ח לכל אחת מהן.
זה משמש למטרות ניתוחים עסקיים, ומאפשר "לסמן" השכרות חריגות בעלותן כדי לבדוק חריגות, להחיל הטבות מיוחדות, או להציג ב־GUI כהשכרות יוקרתיות.

###### Before:
![Update4_before](שלב%20ב/PicturesUPDATE/Update4_bafore.png)

###### Run:
![Update4](שלב%20ב/PicturesUPDATE/Update4.png)

###### After:
![Update4_after](שלב%20ב/PicturesUPDATE/Update4_after.png)

##### 5. UPDATE – שינוי אימיילים של לקוחות שביצעו הכי הרבה תשלומים
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


המערכת מזהה את הלקוחות שביצעו הכי הרבה תשלומים (כלומר היו הכי פעילים) ומעדכנת את כתובת המייל שלהם כך שתכלול את הקידומת vip_.
זה מאפשר זיהוי לקוחות חשובים לצרכים שיווקיים, שירות אישי, או הנחות מיוחדות – והוא חלק מתפיסת CRM (ניהול קשרי לקוחות).

###### Before:
![Update5_before](שלב%20ב/PicturesUPDATE/Update5_before.png)

###### Run:
![Update5](שלב%20ב/PicturesUPDATE/Update5.png)

###### After:
![Update5_after](שלב%20ב/PicturesUPDATE/Update5_after.png)

##### 6. הUPDATE – עדכון טלפונים של סניפים שעם הכי הרבה רכבים
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


השאילתה מזהה את הסניף/ים שיש בהם את מספר הרכבים הגבוה ביותר, ומעדכנת את מספר הטלפון שלהם למספר אחיד (למשל, '03-9999999').
זה שימושי אם החברה רוצה לרכז את הפניות לסניפים הגדולים, או לצורך אחידות בנתונים – לדוגמה במקרה של מוקד שירות לקוחות מרכזי.

###### Before:
![Update6_before](שלב%20ב/PicturesUPDATE/Update6_before.png)

###### Run:
![Update6](שלב%20ב/PicturesUPDATE/Update6.png)

###### After:
![Update6_after](שלב%20ב/PicturesUPDATE/Update6_after.png)


### Constraints

##### 1 אילוץ NOT NULL על טלפון בסניף
ALTER TABLE Branch
ALTER COLUMN Phone SET NOT NULL;


באמצעות הפקודה ALTER TABLE Branch ALTER COLUMN Phone SET NOT NULL, הגדרנו שהשדה Phone בטבלת Branch לא יכול להישאר ריק. כלומר, בכל יצירת רשומה חדשה של סניף – חובה לספק מספר טלפון.
מטרת האילוץ:
לשמור על שלמות המידע ולוודא שלכל סניף ניתן ליצור קשר טלפוני. זה קריטי לפעילות תפעולית ושרות לקוחות.

![Cont1A](שלב%20ב/PicturesConstraints/Cont1A.png)

###### SQL lines that attempted to violate the constraint
![Cont1B](שלב%20ב/PicturesConstraints/Cont1B.png)

##### 2 אילוץ CHECK על סכום תשלום
ALTER TABLE Payment
ADD CONSTRAINT chk_amount_positive CHECK (Amount > 0);


באמצעות ALTER TABLE Payment ADD CONSTRAINT chk_amount_positive CHECK (Amount > 0), הוספנו תנאי בטבלת Payment שמבטיח שסכום התשלום (Amount) חייב להיות חיובי בלבד.
מטרת האילוץ:
מניעת טעויות אנוש או שגיאות מערכת שיגרמו להקלדת תשלומים שליליים או אפסיים, מה שעלול לשבש את המידע הפיננסי.

![Cont2A](שלב%20ב/PicturesConstraints/Cont2A.png)

###### SQL lines that attempted to violate the constraint
![Cont2B](שלב%20ב/PicturesConstraints/Cont2B.png)

##### 3 אילוץ DEFAULT על סטטוס רכב
ALTER TABLE Car
ALTER COLUMN Status SET DEFAULT 'Available';


באמצעות ALTER TABLE Car ALTER COLUMN Status SET DEFAULT 'Available', הוגדר שלרכבים חדשים שיתווספו לטבלת Car, ברירת המחדל לסטטוס תהיה "Available" (זמין).
מטרת האילוץ:
פישוט תהליך ההזנה והנחת עבודה שברירת המחדל לרכב חדש היא שהוא פנוי. זה מקטין סיכוי לשגיאה ומייעל את הזנת הנתונים.

![Cont3A](שלב%20ב/PicturesConstraints/Cont3A.png)

###### SQL lines that meet the constraint
![Cont3B](שלב%20ב/PicturesConstraints/Cont3B.png)

###### After the Changes:
![Cont3C](שלב%20ב/PicturesConstraints/Cont3C.png)

##### אילוץ 4: סכום ההשכרה חייב להיות בהתאם לאורך ההשכרה
ALTER TABLE Rental
ADD CONSTRAINT chk_total_cost_reasonable
CHECK (
    TotalCost >= (DATE_PART('day', EndDate - StartDate) * 100)
);


באמצעות ALTER TABLE Rental ADD CONSTRAINT chk_total_cost_reasonable CHECK (TotalCost >= (DATE_PART('day', EndDate - StartDate) * 100)), נקבע שכל השכרה חייבת להיות במחיר סביר ביחס לאורך ההשכרה – לפחות 100 ש"ח ליום.
מטרת האילוץ:
למנוע טעויות תמחור חמורות כמו השכרה של שבוע במחיר זול מדי. האילוץ מבטיח שכל השכרה מתומחרת בהתאם למשך הזמן שלה.

![Cont4A](שלב%20ב/PicturesConstraints/Cont4A.png)

###### SQL lines that attempted to violate the constraint
![Cont4B](שלב%20ב/PicturesConstraints/Cont4B.png)

##### אילוץ 5: רק לקוחות מעל גיל 18 יכולים להירשם
ALTER TABLE Customer
ADD CONSTRAINT chk_customer_adult
CHECK (
    AGE(CURRENT_DATE, DateOfBirth) >= INTERVAL '18 years'
);


באמצעות ALTER TABLE Customer ADD CONSTRAINT chk_customer_adult CHECK (AGE(CURRENT_DATE, DateOfBirth) >= INTERVAL '18 years'), הוגדר שלקוח יכול להירשם רק אם הוא בן 18 ומעלה.
מטרת האילוץ:
עמידה בתנאי חוקי להחזקת רישיון נהיגה ולהשכרת רכב. האילוץ מוודא שלא יירשמו קטינים שאינם רשאים לנהוג כחוק.

![Cont5A](שלב%20ב/PicturesConstraints/Cont5A.png)

###### SQL lines that attempted to violate the constraint
![Cont5B](שלב%20ב/PicturesConstraints/Cont5B.png)

### Backup2 
-   backups files are kept with the date and hour of the backup:  

[Navigate to the backups folder](שלב%20ב/BackupStage2.backup)
