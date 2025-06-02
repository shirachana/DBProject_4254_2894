CREATE OR REPLACE FUNCTION trg_set_car_status_rented()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE Car SET Status = 'Rented' WHERE CarID = NEW.CarID;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_on_rental_insert
AFTER INSERT ON Rental
FOR EACH ROW
EXECUTE FUNCTION trg_set_car_status_rented();
