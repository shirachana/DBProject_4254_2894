import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from db_config import get_connection

def open_customer_screen():
    window = tk.Toplevel()
    window.title("ניהול לקוחות")
    window.geometry("900x600")

    def close_to_main():
        window.destroy()

    # שדות טופס
    labels = ["Customer ID", "First Name", "Last Name", "Phone", "Email", "License Number", "Date of Birth (YYYY-MM-DD)"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(window, text=label + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(window)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    # טבלת תצוגה
    columns = ("CustomerID", "FirstName", "LastName", "Phone", "Email", "LicenseNumber", "DateOfBirth")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.grid(row=0, column=3, rowspan=10, padx=10, pady=10)

    def clear_fields():
        for entry in entries:
            entry.delete(0, tk.END)

    def insert_customer():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Customer (CustomerID, FirstName, LastName, Phone, Email, LicenseNumber, DateOfBirth)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, tuple(entry.get() for entry in entries))
            conn.commit()
            messagebox.showinfo("הצלחה", "לקוח נוסף בהצלחה")
            cur.close()
            conn.close()
            fetch_customers()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def update_customer():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                UPDATE Customer
                SET FirstName=%s, LastName=%s, Phone=%s, Email=%s, LicenseNumber=%s, DateOfBirth=%s
                WHERE CustomerID=%s
            """, (
                entries[1].get(), entries[2].get(), entries[3].get(),
                entries[4].get(), entries[5].get(), entries[6].get(),
                entries[0].get()
            ))
            conn.commit()
            messagebox.showinfo("הצלחה", "לקוח עודכן בהצלחה")
            cur.close()
            conn.close()
            fetch_customers()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def delete_customer():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Customer WHERE CustomerID = %s", (entries[0].get(),))
            conn.commit()
            messagebox.showinfo("הצלחה", "לקוח נמחק")
            cur.close()
            conn.close()
            fetch_customers()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def fetch_customers():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Customer ORDER BY CustomerID")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    # כפתורים
    tk.Button(window, text="הוספה", width=15, command=insert_customer).grid(row=7, column=0, pady=10)
    tk.Button(window, text="עדכון", width=15, command=update_customer).grid(row=7, column=1)
    tk.Button(window, text="מחיקה", width=15, command=delete_customer).grid(row=8, column=0)
    tk.Button(window, text="רענון", width=15, command=fetch_customers).grid(row=8, column=1)
    tk.Button(window, text="חזרה למסך ראשי", width=25, command=close_to_main).grid(row=9, column=0, columnspan=2, pady=10)

    fetch_customers()
