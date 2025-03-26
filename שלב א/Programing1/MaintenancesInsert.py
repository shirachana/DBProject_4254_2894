import pandas as pd
from faker import Faker
import random
import psycopg2

fake = Faker()

descriptions = [
    "Oil change", "Tire replacement", "Brake inspection",
    "Battery replacement", "Engine tune-up", "Transmission check"
]

try:
    conn = psycopg2.connect(
        host="localhost",  # ← שם השירות בקומפוז (או 'localhost' אם לא בקונטיינר)
        port=5432,
        dbname="RentalCarDB",
        user="shira",
        password="shira2025"  # ← שנה לסיסמה שלך
    )
    cur = conn.cursor()

    # שליפת CarID קיימים
    cur.execute("SELECT CarID FROM Car;")
    car_ids = [row[0] for row in cur.fetchall()]

    maintenances = []
    for i in range(4, 404):
        date = fake.date_between(start_date='-1y', end_date='today')
        desc = random.choice(descriptions)
        cost = round(random.uniform(150.0, 1200.0), 2)
        car_id = random.choice(car_ids)

        maintenances.append([i, date.strftime('%Y-%m-%d'), desc, cost, car_id])

    df = pd.DataFrame(maintenances, columns=[
        "MaintenanceID", "MaintenanceDate", "Description", "MCost", "CarID"
    ])
    df.to_csv("maintenance.csv", index=False, encoding="utf-8")
    print("📁 maintenance.csv נוצר בהצלחה.")

    with open("maintenance.csv", encoding='utf-8') as file:
        next(file)
        cur.copy_expert("""
            COPY Maintenance (MaintenanceID, MaintenanceDate, Description, MCost, CarID)
            FROM STDIN WITH CSV
        """, file)

    conn.commit()
    print("✅ נתוני תחזוקה הוזנו בהצלחה.")

except Exception as e:
    print("❌ שגיאה:", e)

finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()
