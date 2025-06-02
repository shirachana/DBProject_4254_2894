CREATE OR REPLACE FUNCTION update_rental_cost(p_rental_id INT)
RETURNS VOID AS $$
DECLARE
  v_days INT;
  v_price NUMERIC;
BEGIN
  SELECT (EndDate - StartDate), c.PricePerDay
  INTO v_days, v_price
  FROM Rental r
  JOIN Car c ON r.CarID = c.CarID
  WHERE r.RentalID = p_rental_id;

  IF v_days IS NULL THEN
    RAISE EXCEPTION 'השכרה לא קיימת או בעיית תאריכים.';
  END IF;

  UPDATE Rental
  SET TotalCost = GREATEST(v_days, 1) * v_price
  WHERE RentalID = p_rental_id;
END;
$$ LANGUAGE plpgsql;
