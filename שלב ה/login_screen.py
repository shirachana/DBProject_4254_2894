# login_screen.py
import tkinter as tk
from tkinter import messagebox
import subprocess  # כדי להפעיל main.py

def open_login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x180")

    def check_login():
        user = username.get()
        pwd = password.get()
        if user == "admin" and pwd == "admin":
            messagebox.showinfo("הצלחה", "ברוך הבא!")
            root.destroy()  # סוגר את מסך ההתחברות
            subprocess.run(["python", "main.py"])  # מפעיל את הממשק הראשי
        else:
            messagebox.showerror("שגיאה", "פרטי התחברות שגויים")

    tk.Label(root, text="שם משתמש:").pack(pady=5)
    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="סיסמה:").pack(pady=5)
    password = tk.Entry(root, show="*")
    password.pack()

    tk.Button(root, text="התחבר", command=check_login).pack(pady=10)
    root.mainloop()

    # ... כל הקוד של הפונקציה open_login מעל

if __name__ == "__main__":
    open_login()

