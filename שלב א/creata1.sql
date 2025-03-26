CREATE TABLE Customer
(
  CustomerID INT ,
  FirstName VARCHAR(50)  ,
  LastName VARCHAR(50)  ,
  Phone VARCHAR(15)  ,
  Email VARCHAR(100)  ,
  LicenseNumber INT  ,
  DateOfBirth DATE  ,
  PRIMARY KEY (CustomerID),
  UNIQUE (LicenseNumber)
);

CREATE TABLE Payment
(
  PaymentID INT  ,
  PaymentDate DATE  ,
  Amount NUMERIC(10, 2)  ,
  PaymentMethod VARCHAR(15)  ,
  PRIMARY KEY (PaymentID)
);

CREATE TABLE Branch
(
  BranchID INT  ,
  BranchName VARCHAR(100)  ,
  BLocation VARCHAR(255)  ,
  Phone VARCHAR(20)  ,
  PRIMARY KEY (BranchID)
);

CREATE TABLE Car
(
  CarID INT  ,
  LicensePlate INT  ,
  Model VARCHAR(50)  ,
  Manufacturer VARCHAR(50)  ,
  CYear INT  ,
  Status VARCHAR(20)  ,
  PricePerDay NUMERIC(10, 2)  ,
  NumSeats INT  ,
  BranchID INT  ,
  PRIMARY KEY (CarID),
  FOREIGN KEY (BranchID) REFERENCES Branch(BranchID),
  UNIQUE (LicensePlate)
);

CREATE TABLE Rental
(
  RentalID INT  ,
  StartDate DATE  ,
  EndDate DATE  ,
  TotalCost INT  ,
  CustomerID INT  ,
  CarID INT  ,
  PaymentID INT  ,
  PRIMARY KEY (RentalID),
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
  FOREIGN KEY (CarID) REFERENCES Car(CarID),
  FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID),
  UNIQUE (CustomerID),
  UNIQUE (CarID)
);

CREATE TABLE Maintenance
(
  MaintenanceID INT  ,
  MaintenanceDate DATE  ,
  Description VARCHAR(255)  ,
  MCost NUMERIC(10, 2)  ,
  CarID INT  ,
  PRIMARY KEY (MaintenanceID),
  FOREIGN KEY (CarID) REFERENCES Car(CarID)
);