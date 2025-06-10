# main.py
import tkinter as tk
from tkinter import ttk
from login_screen import open_login

root = tk.Tk()
root.title("Rental Car System - Main")
root.geometry("400x300")

def open_customers():
    from customer_crud import open_customer_screen
    open_customer_screen()

def open_cars():
    from car_crud import open_car_screen
    open_car_screen()

def open_rentals():
    from rental_crud import open_rental_screen
    open_rental_screen()

def open_reports():
    from reports_screen import open_report_screen
    open_report_screen()

def logout():
    root.withdraw()  # הסתרת המסך הראשי
    open_login()     # פתיחת מסך התחברות מחדש    

# GUI
tk.Label(root, text="מערכת ניהול השכרות", font=("Helvetica", 16)).pack(pady=10)
tk.Button(root, text="ניהול לקוחות", width=25, command=open_customers).pack(pady=5)
tk.Button(root, text="ניהול רכבים", width=25, command=open_cars).pack(pady=5)
tk.Button(root, text="ניהול השכרות", width=25, command=open_rentals).pack(pady=5)
tk.Button(root, text="דוחות ושאילתות", width=25, command=open_reports).pack(pady=5)
tk.Button(root, text="התנתק", width=25, command=logout).pack(pady=20)

root.mainloop()
