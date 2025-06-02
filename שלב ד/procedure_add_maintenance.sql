CREATE OR REPLACE PROCEDURE add_maintenance(
  p_carid INT,
  p_description VARCHAR,
  p_cost NUMERIC,
  p_date DATE
)
AS $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM Car WHERE CarID = p_carid) THEN
    RAISE EXCEPTION 'רכב לא קיים';
  END IF;

  INSERT INTO Maintenance (MaintenanceID, MaintenanceDate, Description, MCost, CarID)
  VALUES (DEFAULT, p_date, p_description, p_cost, p_carid);
END;
$$ LANGUAGE plpgsql;
