CREATE OR REPLACE FUNCTION log_rental_delete()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO log_deleted_rentals(RentalID) VALUES (OLD.RentalID);
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_rental_delete
AFTER DELETE ON Rental
FOR EACH ROW
EXECUTE FUNCTION log_rental_delete();
