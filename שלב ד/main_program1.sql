DO $$
BEGIN
  PERFORM update_rental_cost(101);
  CALL add_maintenance(5, 'בדיקת בלמים', 280.00, CURRENT_DATE);
END;
$$;
