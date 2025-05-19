CREATE EXTENSION IF NOT EXISTS postgres_fdw;


CREATE SERVER triporg_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'localhost', dbname 'TRIPORG', port '5432');

CREATE USER MAPPING FOR shira
SERVER tripOrgDB_server
OPTIONS (user 'shira', password 'shira2025');


CREATE FOREIGN TABLE trip_remote (

  tripid INT,
  startdate DATE,
  enddate DATE,
  destinationzip INT,
  hotelid INT,
  guideid INT,
  flightid INT
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'trip');

CREATE FOREIGN TABLE guide_remote (
  guideid INT,
  guidename VARCHAR(100),
  phonenumber VARCHAR(20)
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'guide');

CREATE FOREIGN TABLE hotel_remote (
  hotelid INT,
  hotelname VARCHAR(100),
  location VARCHAR(255),
  totalrooms INT
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'hotel');

CREATE FOREIGN TABLE flight_remote (
  flightid INT,
  airline VARCHAR(100),
  depaturedate DATE,
  returndate DATE
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'flight');

CREATE FOREIGN TABLE destination_remote (
  zipcode INT,
  country VARCHAR(100),
  address VARCHAR(255)
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'destination');

CREATE FOREIGN TABLE invite_remote (
  tripid INT,
  customerid INT,
  totalcustomer INT
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'invite');

CREATE FOREIGN TABLE customer_remote (
  id INT,
  fullname VARCHAR(100),
  phonenumber VARCHAR(20),
  email VARCHAR(100)
) SERVER tripOrgDB_server
OPTIONS (schema_name 'public', table_name 'customer');

INSERT INTO Customer (CustomerID, FirstName, LastName, Phone, Email, LicenseNumber, DateOfBirth)
SELECT
  id,
  split_part(fullname, ' ', 1),
  split_part(fullname, ' ', 2),
  phonenumber,
  email,
  floor(random() * 900000000 + 100000000)::INT,
  (CURRENT_DATE - (18 + floor(random() * 40)) * INTERVAL '1 year')::DATE
FROM customer_remote
ON CONFLICT (CustomerID) DO NOTHING;

