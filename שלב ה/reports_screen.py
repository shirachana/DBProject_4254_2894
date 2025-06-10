import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import psycopg2
from db_config import get_connection

def open_report_screen():
    window = tk.Toplevel()
    window.title("דוחות ושאילתות")
    window.geometry("1100x600")

    # טבלת תוצאות
    tree = ttk.Treeview(window)
    tree.pack(pady=20, fill="both", expand=True)

    def display_results(columns, data):
        tree.delete(*tree.get_children())
        tree["columns"] = columns
        tree["show"] = "headings"
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        for row in data:
            tree.insert("", "end", values=row)

    def run_query(sql, params=()):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(sql, params)
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            display_results(colnames, rows)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    def run_function_with_param():
        age = simpledialog.askinteger("פונקציה", "הכנס גיל:")
        if age is not None:
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.callproc("get_customers_above_age", (age,))
                cur.execute("FETCH ALL IN cust_cursor")
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                display_results(colnames, rows)
                cur.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

    def run_update_rental_cost():
        rental_id = simpledialog.askinteger("עדכון עלות", "הכנס מזהה השכרה:")
        if rental_id:
            try:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("SELECT update_rental_cost(%s)", (rental_id,))
                conn.commit()
                cur.execute("SELECT * FROM Rental WHERE RentalID = %s", (rental_id,))
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                display_results(colnames, rows)
                cur.close()
                conn.close()
                messagebox.showinfo("הצלחה", f"השכרה מספר {rental_id} עודכנה בהצלחה")
            except Exception as e:
                messagebox.showerror("שגיאה", str(e))

    def run_add_maintenance():
        try:
            car_id = simpledialog.askinteger("רכב", "הכנס מזהה רכב:")
            desc = simpledialog.askstring("תיאור", "הכנס תיאור תחזוקה:")
            cost = simpledialog.askfloat("מחיר", "הכנס מחיר תחזוקה:")
            date = simpledialog.askstring("תאריך", "הכנס תאריך (YYYY-MM-DD):")

            if car_id and desc and cost and date:
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("CALL add_maintenance(%s, %s, %s, %s)", (car_id, desc, cost, date))
                conn.commit()
                messagebox.showinfo("הצלחה", "תחזוקה נוספה בהצלחה.")
                cur.execute("SELECT * FROM Maintenance WHERE CarID = %s ORDER BY MaintenanceDate DESC LIMIT 5", (car_id,))
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                display_results(colnames, rows)
                cur.close()
                conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    def run_branch_car_summary():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM branch_car_summary_func()")
            rows = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]
            display_results(colnames, rows)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    # רשימת שאילתות
    queries = {
        "1. רכבים שהושכרו ב-2025 עם פרטי לקוח":
            """SELECT c.FirstName, c.LastName, car.Model, car.Manufacturer, r.StartDate, r.EndDate
               FROM Rental r
               JOIN Customer c ON r.CustomerID = c.CustomerID
               JOIN Car car ON r.CarID = car.CarID
               WHERE r.StartDate >= '2025-01-01' AND r.EndDate <= '2025-12-31'""",

        "2. חודשים עם השכרות מעל ממוצע":
            """SELECT EXTRACT(YEAR FROM StartDate) AS Year,
                      EXTRACT(MONTH FROM StartDate) AS Month,
                      COUNT(*) AS TotalRentals
               FROM Rental
               GROUP BY Year, Month
               HAVING COUNT(*) > (
                   SELECT AVG(MonthlyCount) FROM (
                       SELECT COUNT(*) AS MonthlyCount
                       FROM Rental
                       GROUP BY EXTRACT(YEAR FROM StartDate), EXTRACT(MONTH FROM StartDate)
                   ) AS MonthlyData
               )
               ORDER BY Year, Month""",

        "3. ממוצע מושבים לרכבים שהושכרו":
            """SELECT AVG(car.NumSeats) AS AvgSeats
               FROM Rental r
               JOIN Car car ON r.CarID = car.CarID""",

        "4. רכבים ללא תחזוקה":
            """SELECT car.CarID, car.Model
               FROM Car car
               LEFT JOIN Maintenance m ON car.CarID = m.CarID
               WHERE m.MaintenanceID IS NULL"""
    }

    tk.Label(window, text="בחר שאילתה:").pack()
    query_combo = ttk.Combobox(window, values=list(queries.keys()), width=70)
    query_combo.pack(pady=5)

    def execute_selected_query():
        selected = query_combo.get()
        if selected in queries:
            run_query(queries[selected])

    tk.Button(window, text="הרץ שאילתה", command=execute_selected_query).pack(pady=10)

    # פונקציות ופרוצדורות
    tk.Label(window, text="פונקציות ופרוצדורות מתקדמות:").pack(pady=10)
    tk.Button(window, text="פונקציה: לקוחות מעל גיל נתון", command=run_function_with_param).pack(pady=5)
    tk.Button(window, text="פונקציה: עדכון עלות השכרה לפי מזהה", command=run_update_rental_cost).pack(pady=5)
    tk.Button(window, text="פרוצדורה: הוספת תחזוקה", command=run_add_maintenance).pack(pady=5)
    tk.Button(window, text="סיכום רכבים לפי סניף", command=run_branch_car_summary).pack(pady=5)

    # חזרה
    tk.Button(window, text="חזור למסך הראשי", command=window.destroy).pack(pady=20)
