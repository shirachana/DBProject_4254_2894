-- Branch
INSERT INTO Branch VALUES (1, 'Tel Aviv Central', 'Dizengoff 100, Tel Aviv', '03-5551234');
INSERT INTO Branch VALUES (2, 'Jerusalem East', 'King George 23, Jerusalem', '02-7778888');
INSERT INTO Branch VALUES (3, 'Haifa Bay', 'HaMifratz 12, Haifa', '04-8889999');

-- Customer
INSERT INTO Customer VALUES (1, 'David', 'Levi', '0501234567', 'david@example.com', 123456789, '1990-05-01');
INSERT INTO Customer VALUES (2, 'Maya', 'Cohen', '0509876543', 'maya@example.com', 987654321, '1985-12-11');
INSERT INTO Customer VALUES (3, 'Noa', 'Bar', '0504567890', 'noa@example.com', 555444333, '1993-07-21');

-- Payment
INSERT INTO Payment VALUES (1, '2025-03-01', 320.50, 'Credit');
INSERT INTO Payment VALUES (2, '2025-03-02', 150.00, 'Cash');
INSERT INTO Payment VALUES (3, '2025-03-03', 270.75, 'PayPal');

-- Car
INSERT INTO Car VALUES (1, 1111111, 'Corolla', 'Toyota', 2020, 'Available', 130.00, 5, 1);
INSERT INTO Car VALUES (2, 2222222, 'Civic', 'Honda', 2019, 'Rented', 150.00, 5, 2);
INSERT INTO Car VALUES (3, 3333333, 'Model 3', 'Tesla', 2021, 'In Maintenance', 300.00, 5, 3);

-- Rental
INSERT INTO Rental VALUES (1, '2025-03-10', '2025-03-13', 390, 1, 2, 1);
INSERT INTO Rental VALUES (2, '2025-03-15', '2025-03-16', 150, 2, 1, 2);
INSERT INTO Rental VALUES (3, '2025-03-20', '2025-03-22', 600, 3, 3, 3);

-- Maintenance
INSERT INTO Maintenance VALUES (1, '2025-02-10', 'Oil change and filter replacement', 200.00, 1);
INSERT INTO Maintenance VALUES (2, '2025-02-20', 'Tire replacement', 600.00, 2);
INSERT INTO Maintenance VALUES (3, '2025-03-01', 'Brake pad replacement', 450.00, 3);

