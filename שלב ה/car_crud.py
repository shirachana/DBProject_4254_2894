
import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from db_config import get_connection

def open_car_screen():
    window = tk.Toplevel()
    window.title("ניהול רכבים")
    window.geometry("900x600")

    def close_to_main():
        window.destroy()

    labels = ["Car ID", "Model", "Manufacturer", "NumSeats", "Status", "PricePerDay", "BranchID"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(window, text=label + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(window)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    columns = ("CarID", "Model", "Manufacturer", "NumSeats", "Status", "PricePerDay", "BranchID")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.grid(row=0, column=3, rowspan=10, padx=10, pady=10)

    def clear_fields():
        for entry in entries:
            entry.delete(0, tk.END)

    def insert_car():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO Car (CarID, Model, Manufacturer, NumSeats, Status, PricePerDay, BranchID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        tuple(entry.get() for entry in entries))
            conn.commit()
            messagebox.showinfo("הצלחה", "רכב נוסף")
            cur.close()
            conn.close()
            fetch_cars()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def update_car():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("UPDATE Car SET Model=%s, Manufacturer=%s, NumSeats=%s, Status=%s, PricePerDay=%s, BranchID=%s WHERE CarID=%s",
                        (entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get(), entries[5].get(), entries[6].get(), entries[0].get()))
            conn.commit()
            messagebox.showinfo("הצלחה", "רכב עודכן")
            cur.close()
            conn.close()
            fetch_cars()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def delete_car():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Car WHERE CarID=%s", (entries[0].get(),))
            conn.commit()
            messagebox.showinfo("הצלחה", "רכב נמחק")
            cur.close()
            conn.close()
            fetch_cars()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def fetch_cars():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Car ORDER BY CarID")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    tk.Button(window, text="הוספה", width=15, command=insert_car).grid(row=7, column=0, pady=10)
    tk.Button(window, text="עדכון", width=15, command=update_car).grid(row=7, column=1)
    tk.Button(window, text="מחיקה", width=15, command=delete_car).grid(row=8, column=0)
    tk.Button(window, text="רענון", width=15, command=fetch_cars).grid(row=8, column=1)
    tk.Button(window, text="חזרה למסך ראשי", width=25, command=close_to_main).grid(row=9, column=0, columnspan=2, pady=10)

    fetch_cars()
