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
- [Phase 2: Integration](#phase-2-integration)  

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
![ERD Diagram](Pictures\ERD.png)

###  DSD (Data Structure Diagram)   
![DSD Diagram](Pictures\DSD.png)  

### ERD Pgadmin
![ERD - PG](Pictures\ERDPG.png)

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

![image1](Pictures\image.png)

![image2](Pictures\image-1.png)

results for  the command `SELECT 'Branch' AS TableName, COUNT(*) FROM Branch;`:
![image3](Pictures\image-2.png) 

##### Payments Table Data Entry:
• Payment ID: 4–23
📜**[View `payments2.csv`](שלב%20א/DataImportFiles/payments2.csv)**

![image4](Pictures\image-3.png)

![image5](Pictures\image-4.png)
#### Second tool: using [generatedata](https://generatedata.com/generator). to create csv file
##### Payments Table Data Entry:
• Payment ID: 24-396
📜**[View `PaymentsInsert1.csv`](שלב%20א/generatedataFiles/PaymentsInsert1.csv)**

![image6](Pictures\image-5.png)

![image7](Pictures\image-6.png)

![image8](Pictures\image-7.png)

results for  the command `SELECT 'Payment' AS TableName, COUNT(*) FROM Payment;`:
![image9](Pictures\image-8.png)

####  Third tool: using [mockaro](https://www.mockaroo.com/) to create csv file
##### Car Table Data Entry:
• Car ID: 4–403
-  Formula of Car ID: `this + 4`
📜 **[View `mock_car.csv`](שלב%20א/mockarooFiles/mock_car.csv)**

![image10](Pictures\image-9.png)

![image11](Pictures\image-10.png)

![alt text](<תמונה של WhatsApp‏ 2025-03-29 בשעה 23.01.14_eb709eab.jpg>)

results for  the command `SELECT 'Car' AS TableName, COUNT(*) FROM Car;`:
![image12](Pictures\image-11.png)

####  Fourth Tool: Using Python to generate a CSV file and insert it into the database
##### Customers Table Data Entry:
• Customer ID: 4–403
📜 **[View `customers.csv`](שלב%20א/Programing1/customers.csv)**

**[View `CustomersInsert.py`](שלב%20א/Programing1/CustomerInsert.py)**

![image13](Pictures\image-12.png)

results for  the command `SELECT 'Customer' AS TableName, COUNT(*) FROM Customer;`:
![image14](Pictures\image-13.png)

##### Rental Table Data Entry:
• Rental ID: 4–403
📜 **[View `rentals.csv`](שלב%20א/Programing1/rentals.csv)**

**[View `RentalInsert.py`](שלב%20א/Programing1/RentalInsert.py)**

![alt1 text](Pictures/תמונה%20של%20WhatsApp‏%202025-03-29%20בשעה%2023.58.27_06a936d2.jpg)

![image15](Pictures\image-14.png)

results for  the command `SELECT 'Rental' AS TableName, COUNT(*) FROM Rental;`:
![image16](Pictures\image-15.png)

##### Maintenance Table Data Entry:
• Maintenance ID: 4–403
📜 **[View `maintenance.csv`](שלב%20א/Programing1/maintenance.csv)**

**[View `MaintenanceInsert.py`](שלב%20א/Programing1/MaintenancesInsert.py)**

![alt3 text](Pictures/תמונה%20של%20WhatsApp‏%202025-03-29%20בשעה%2023.59.18_245283a0.jpg)

![image17](Pictures\image-16.png)

results for  the command `SELECT 'Maintenance' AS TableName, COUNT(*) FROM Maintenance;`:
![image18](Pictures\image-17.png)
### Backup 
-   backups files are kept with the date and hour of the backup:  

[Navigate to the backups folder](שלב%20א/Backup2.backup)

[Also backups folder](שלב%20א/Backup.sql)

![image19](Pictures\image-18.png)

### Data Restoration

![image20](Pictures\image-19.png)


## Phase 2: Integration 
