import pandas as pd
from faker import Faker
import random
import psycopg2
from datetime import timedelta

fake = Faker()

try:
    conn = psycopg2.connect(
        host="localhost",  # ← שם השירות בקומפוז (או 'localhost' אם לא בקונטיינר)
        port=5432,
        dbname="RentalCarDB",
        user="shira",
        password="shira2025"  # ← שנה לסיסמה שלך
    )
    cur = conn.cursor()

    # שליפת כל מזהי Customer / Car / Payment
    cur.execute("SELECT CustomerID FROM Customer;")
    customer_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT CarID FROM Car;")
    car_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT PaymentID FROM Payment;")
    payment_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT CarID, PricePerDay FROM Car;")
    car_price_map = {row[0]: float(row[1]) for row in cur.fetchall()}

    # שליפת מזהים שכבר בשימוש
    cur.execute("SELECT CustomerID FROM Rental;")
    used_customer_ids = set(row[0] for row in cur.fetchall())

    cur.execute("SELECT CarID FROM Rental;")
    used_car_ids = set(row[0] for row in cur.fetchall())

    cur.execute("SELECT COUNT(*) FROM Rental;")
    existing_rentals = cur.fetchone()[0]

    # כמה להשלים?
    missing = 400 - existing_rentals
    if missing <= 0:
        print("✅ כבר קיימות 400 השכרות. אין צורך להוסיף.")
        cur.close()
        conn.close()
        exit()

    # בחירת מזהים זמינים
    available_customer_ids = list(set(customer_ids) - used_customer_ids)
    available_car_ids = list(set(car_ids) - used_car_ids)

    if len(available_customer_ids) < missing or len(available_car_ids) < missing:
        raise Exception("❗ אין מספיק מזהים זמינים ליצירת שורות Rental נוספות.")

    selected_customer_ids = random.sample(available_customer_ids, missing)
    selected_car_ids = random.sample(available_car_ids, missing)

    rentals = []
    start_rental_id = existing_rentals + 4  # מתחילים מה-ID הבא

    for i in range(missing):
        rental_id = start_rental_id + i
        start_date = fake.date_between(start_date='-1y', end_date='-5d')
        end_date = start_date + timedelta(days=random.randint(1, 10))
        num_days = (end_date - start_date).days

        customer_id = selected_customer_ids[i]
        car_id = selected_car_ids[i]
        payment_id = random.choice(payment_ids)

        price_per_day = car_price_map.get(car_id, 0)
        total_cost = round(num_days * price_per_day, 2)

        rentals.append([
            rental_id, start_date.strftime('%Y-%m-%d'),
            end_date.strftime('%Y-%m-%d'),
            total_cost, customer_id, car_id, payment_id
        ])

    # שמירה לקובץ CSV
    df = pd.DataFrame(rentals, columns=[
        "RentalID", "StartDate", "EndDate", "TotalCost", "CustomerID", "CarID", "PaymentID"
    ])
    df.to_csv("rentals.csv", index=False, encoding="utf-8")
    print(f"📁 rentals.csv נוצר עם {missing} שורות חדשות.")

    # טעינה למסד
    with open("rentals.csv", encoding='utf-8') as file:
        next(file)
        cur.copy_expert("""
            COPY Rental (RentalID, StartDate, EndDate, TotalCost, CustomerID, CarID, PaymentID)
            FROM STDIN WITH CSV
        """, file)

    conn.commit()
    print("✅ ההשכרות הוזנו למסד בהצלחה.")

except Exception as e:
    print("❌ שגיאה:", e)

finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()
