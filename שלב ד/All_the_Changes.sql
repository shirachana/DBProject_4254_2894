CREATE TABLE log_deleted_rentals (
  RentalID INT,
  DeletedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- שינוי העמודה
ALTER TABLE Maintenance 
ALTER COLUMN MaintenanceID DROP DEFAULT;

-- יצירת רצף (אם לא קיים)
CREATE SEQUENCE IF NOT EXISTS maintenance_id_seq;

-- חיבור הרצף לעמודה
ALTER TABLE Maintenance 
ALTER COLUMN MaintenanceID SET DEFAULT nextval('maintenance_id_seq');