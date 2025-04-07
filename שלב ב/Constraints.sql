-- 1 אילוץ NOT NULL על טלפון בסניף
ALTER TABLE Branch
ALTER COLUMN Phone SET NOT NULL;

-- 2 אילוץ CHECK על סכום תשלום
ALTER TABLE Payment
ADD CONSTRAINT chk_amount_positive CHECK (Amount > 0);

-- 3 אילוץ DEFAULT על סטטוס רכב
ALTER TABLE Car
ALTER COLUMN Status SET DEFAULT 'Available';

-- אילוץ 4: סכום ההשכרה חייב להיות בהתאם לאורך ההשכרה
ALTER TABLE Rental
ADD CONSTRAINT chk_total_cost_reasonable
CHECK (
    TotalCost >= (DATE_PART('day', EndDate - StartDate) * 100)
);

-- אילוץ 5: רק לקוחות מעל גיל 18 יכולים להירשם
ALTER TABLE Customer
ADD CONSTRAINT chk_customer_adult
CHECK (
    AGE(CURRENT_DATE, DateOfBirth) >= INTERVAL '18 years'
);
