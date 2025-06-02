DO $$
DECLARE
  ref refcursor;
  row RECORD;
BEGIN
  ref := get_customers_above_age(60);
  LOOP
    FETCH ref INTO row;
    EXIT WHEN NOT FOUND;
    RAISE NOTICE 'לקוח: % %', row.FirstName, row.LastName;
  END LOOP;

  CALL branch_car_summary();
END;
$$;
