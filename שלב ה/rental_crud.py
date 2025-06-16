import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import psycopg2
from db_config import get_connection

def open_rental_screen():
    window = tk.Toplevel()
    window.title("ניהול השכרות")
    window.geometry("1100x650")

    def close_to_main():
        window.destroy()

    # --- שליפת רשימות מה-DB עבור ComboBox ---
    def get_customers():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT customerid, firstname, lastname FROM customer ORDER BY customerid")
        data = cur.fetchall()
        cur.close()
        conn.close()
        # רשימה של tuples: (id, תיאור לתצוגה)
        return [(str(cid), f"{cid} - {fname} {lname}") for cid, fname, lname in data]

    def get_cars():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT carid, model, manufacturer FROM car ORDER BY carid")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return [(str(cid), f"{cid} - {manu} {model}") for cid, model, manu in data]

    def get_payments():
     try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT paymentid FROM payment ORDER BY paymentid")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return [(str(pid[0]), str(pid[0])) for pid in data]
     except Exception as e:
        messagebox.showerror("שגיאה בשליפת תשלומים", str(e))
        return []


    # שליפת ערכי הקומבובוקסים
    customer_options = get_customers()
    car_options = get_cars()
    payment_options = get_payments()

    # --- הגדרת שדות וממשק ---
    labels = ["Rental ID", "לקוח", "רכב", "תאריך התחלה", "תאריך סיום", "TotalCost", "תשלום"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(window, text=label + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
        if i == 1:  # לקוח
            cb = ttk.Combobox(window, state="readonly", values=[opt[1] for opt in customer_options])
            cb.grid(row=i, column=1, padx=5, pady=5)
            entries.append(cb)
        elif i == 2:  # רכב
            cb = ttk.Combobox(window, state="readonly", values=[opt[1] for opt in car_options])
            cb.grid(row=i, column=1, padx=5, pady=5)
            entries.append(cb)
        elif i == 3 or i == 4:  # תאריכים
            date_entry = DateEntry(window, date_pattern='yyyy-mm-dd')
            date_entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(date_entry)
        elif i == 6:  # תשלום
            cb = ttk.Combobox(window, state="readonly", values=[opt[1] for opt in payment_options])
            cb.grid(row=i, column=1, padx=5, pady=5)
            entries.append(cb)
        else:
            entry = tk.Entry(window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

    columns = ("RentalID", "CustomerID", "CarID", "StartDate", "EndDate", "TotalCost", "PaymentID")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=18)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.grid(row=0, column=3, rowspan=12, padx=10, pady=10)

    def clear_fields():
        for i, entry in enumerate(entries):
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            elif isinstance(entry, DateEntry):
                entry.set_date('')
            else:
                entry.delete(0, tk.END)

    def insert_rental():
     try:
        customer_idx = entries[1].current()
        car_idx = entries[2].current()
        payment_idx = entries[6].current()
        if customer_idx == -1 or car_idx == -1 or payment_idx == -1:
            messagebox.showerror("שגיאה", "יש לבחור ערך בכל הרשימות!")
            return

        customer_id = customer_options[customer_idx][0]
        car_id = car_options[car_idx][0]
        payment_id = payment_options[payment_idx][0]

        data = (
            customer_id,
            car_id,
            entries[3].get_date(),  # StartDate
            entries[4].get_date(),  # EndDate
            entries[5].get(),       # TotalCost
            payment_id
        )

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Rental (customerid, carid, startdate, enddate, totalcost, paymentid)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, data)
        conn.commit()
        messagebox.showinfo("הצלחה", "השכרה נוספה")
        cur.close()
        conn.close()
        fetch_rentals()
        clear_fields()
     except Exception as e:
        messagebox.showerror("שגיאה", str(e))


    def update_rental():
        try:
            customer_idx = entries[1].current()
            car_idx = entries[2].current()
            payment_idx = entries[6].current()
            if customer_idx == -1 or car_idx == -1 or payment_idx == -1:
                messagebox.showerror("שגיאה", "יש לבחור ערך בכל הרשימות!")
                return
            customer_id = customer_options[customer_idx][0]
            car_id = car_options[car_idx][0]
            payment_id = payment_options[payment_idx][0]
            data = (
                customer_id,
                car_id,
                entries[3].get_date(),  # StartDate
                entries[4].get_date(),  # EndDate
                entries[5].get(),  # TotalCost
                payment_id,
                entries[0].get()   # RentalID
            )
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE Rental
                SET customerid=%s, carid=%s, startdate=%s, enddate=%s, totalcost=%s, paymentid=%s
                WHERE rentalid=%s
            """, data)
            conn.commit()
            messagebox.showinfo("הצלחה", "השכרה עודכנה")
            cur.close()
            conn.close()
            fetch_rentals()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    def delete_rental():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Rental WHERE rentalid=%s", (entries[0].get(),))
            conn.commit()
            messagebox.showinfo("הצלחה", "השכרה נמחקה")
            cur.close()
            conn.close()
            fetch_rentals()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    def fetch_rentals():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT rentalid, customerid, carid, startdate, enddate, totalcost, paymentid FROM rental ORDER BY rentalid")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    tk.Button(window, text="הוספה", width=15, command=insert_rental).grid(row=8, column=0, pady=10)
    tk.Button(window, text="עדכון", width=15, command=update_rental).grid(row=8, column=1)
    tk.Button(window, text="מחיקה", width=15, command=delete_rental).grid(row=9, column=0)
    tk.Button(window, text="רענון", width=15, command=fetch_rentals).grid(row=9, column=1)
    tk.Button(window, text="חזרה למסך ראשי", width=25, command=close_to_main).grid(row=10, column=0, columnspan=2, pady=10)

    fetch_rentals()
