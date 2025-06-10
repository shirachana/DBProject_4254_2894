# db_config.py
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",             # ← שם השירות בקומפוז (או 'localhost' אם לא בקונטיינר)
        port=5432,
        dbname="RentalCarDB",
        user="shira",
        password="shira2025"  # ← שנה לסיסמה שלך
    )
