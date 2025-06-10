
import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from db_config import get_connection

def open_rental_screen():
    window = tk.Toplevel()
    window.title("ניהול השכרות")
    window.geometry("1000x600")

    def close_to_main():
        window.destroy()

    labels = ["Rental ID", "CustomerID", "CarID", "StartDate (YYYY-MM-DD)", "EndDate (YYYY-MM-DD)", "TotalCost", "PaymentID"]
    entries = []
    for i, label in enumerate(labels):
        tk.Label(window, text=label + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(window)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    columns = ("RentalID", "CustomerID", "CarID", "StartDate", "EndDate", "TotalCost", "PaymentID")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.grid(row=0, column=3, rowspan=10, padx=10, pady=10)

    def clear_fields():
        for entry in entries:
            entry.delete(0, tk.END)

    def insert_rental():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO Rental (RentalID, CustomerID, CarID, StartDate, EndDate, TotalCost, PaymentID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        tuple(entry.get() for entry in entries))
            conn.commit()
            messagebox.showinfo("הצלחה", "השכרה נוספה")
            cur.close()
            conn.close()
            fetch_rentals()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def update_rental():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("UPDATE Rental SET CustomerID=%s, CarID=%s, StartDate=%s, EndDate=%s, TotalCost=%s, PaymentID=%s WHERE RentalID=%s",
                        (entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get(), entries[5].get(), entries[6].get(), entries[0].get()))
            conn.commit()
            messagebox.showinfo("הצלחה", "השכרה עודכנה")
            cur.close()
            conn.close()
            fetch_rentals()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def delete_rental():
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Rental WHERE RentalID=%s", (entries[0].get(),))
            conn.commit()
            messagebox.showinfo("הצלחה", "השכרה נמחקה")
            cur.close()
            conn.close()
            fetch_rentals()
            clear_fields()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))
            close_to_main()

    def fetch_rentals():
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Rental ORDER BY RentalID")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", str(e))

    tk.Button(window, text="הוספה", width=15, command=insert_rental).grid(row=7, column=0, pady=10)
    tk.Button(window, text="עדכון", width=15, command=update_rental).grid(row=7, column=1)
    tk.Button(window, text="מחיקה", width=15, command=delete_rental).grid(row=8, column=0)
    tk.Button(window, text="רענון", width=15, command=fetch_rentals).grid(row=8, column=1)
    tk.Button(window, text="חזרה למסך ראשי", width=25, command=close_to_main).grid(row=9, column=0, columnspan=2, pady=10)

    fetch_rentals()
