CREATE OR REPLACE FUNCTION get_customers_above_age(p_age INT)
RETURNS refcursor AS $$
DECLARE
  cur refcursor := 'cust_cursor';
BEGIN
  OPEN cur FOR
    SELECT CustomerID, FirstName, LastName, DateOfBirth,
           EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) AS Age
    FROM Customer
    WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, DateOfBirth)) > p_age;
  RETURN cur;
END;
$$ LANGUAGE plpgsql;
