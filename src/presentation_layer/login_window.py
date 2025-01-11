import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.user_management import User


class LoginWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Login")
        self.master.geometry("600x400")

        # Username Label and Entry
        tk.Label(master, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(master, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(master, text="Login", command=self.authenticate_user).pack(pady=20)

    def authenticate_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Validate user input
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # Check credentials against the database
        db = next(get_db())  # Get a session
        try:
            user = db.query(User).filter_by(username=username, is_admin=True).first()
            if user and user.password == password:
                messagebox.showinfo("Success", "Login successful!")
                self.controller.show_main_window()  # Replace with the main application window
            else:
                messagebox.showerror("Error", "Invalid credentials.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            db.close()
