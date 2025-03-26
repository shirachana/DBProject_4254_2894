import pandas as pd
from faker import Faker
import random
import psycopg2

# יצירת לקוחות
fake = Faker('he_IL')
customers = []

for i in range(4, 404):  # 400 לקוחות מ-4 עד 403
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.phone_number().replace(" ", "").replace("-", "")
    email = fake.email()
    license_number = fake.unique.random_int(min=1000000, max=9999999)
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=75).strftime('%Y-%m-%d')

    customers.append([i, first_name, last_name, phone, email, license_number, birth_date])

# שמירה לקובץ CSV
df = pd.DataFrame(customers, columns=[
    "CustomerID", "FirstName", "LastName", "Phone", "Email", "LicenseNumber", "DateOfBirth"
])
df.to_csv("customers.csv", index=False, encoding="utf-8")
print("📁 customers.csv נוצר בהצלחה.")

# התחברות למסד הנתונים
try:
    conn = psycopg2.connect(
        host="localhost",             # ← שם השירות בקומפוז (או 'localhost' אם לא בקונטיינר)
        port=5432,
        dbname="RentalCarDB",
        user="shira",
        password="shira2025"  # ← שנה לסיסמה שלך
    )
    cur = conn.cursor()

    # טעינת הנתונים מתוך הקובץ
    with open("customers.csv", encoding='utf-8') as file:
        next(file)  # דילוג על שורת כותרת
        cur.copy_expert("""
            COPY Customer (CustomerID, FirstName, LastName, Phone, Email, LicenseNumber, DateOfBirth)
            FROM STDIN WITH CSV
        """, file)

    conn.commit()
    print("✅ כל הלקוחות הוזנו בהצלחה למסד הנתונים.")

except Exception as e:
    print("❌ שגיאה:", e)

finally:
    cur.close()
    conn.close()
