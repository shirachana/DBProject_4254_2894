CREATE OR REPLACE PROCEDURE branch_car_summary()
AS $$
DECLARE
  rec RECORD;
  cur CURSOR FOR
    SELECT b.BranchName, COUNT(*) AS CarCount
    FROM Branch b
    JOIN Car c ON b.BranchID = c.BranchID
    GROUP BY b.BranchName;
BEGIN
  OPEN cur;
  LOOP
    FETCH cur INTO rec;
    EXIT WHEN NOT FOUND;
    RAISE NOTICE 'סניף: %, מספר רכבים: %', rec.BranchName, rec.CarCount;
  END LOOP;
  CLOSE cur;
END;
$$ LANGUAGE plpgsql;
