import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.user_management import User


class UserManagementWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("User Management")
        self.master.geometry("600x400")

        # Title
        tk.Label(master, text="User Management", font=("Arial", 16)).pack(pady=10)

        # Buttons for different user management functionalities
        tk.Button(master, text="Add User", width=20, command=self.add_user).pack(pady=5)
        tk.Button(master, text="Update User", width=20, command=self.update_user).pack(pady=5)
        tk.Button(master, text="Delete User", width=20, command=self.delete_user).pack(pady=5)
        tk.Button(master, text="View All Users", width=20, command=self.view_all_users).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back to Dashboard", width=20, command=self.controller.show_dashboard_window).pack(pady=20)

    def add_user(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add User")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Username:").pack(pady=5)
        username_entry = tk.Entry(add_window)
        username_entry.pack(pady=5)

        tk.Label(add_window, text="Password:").pack(pady=5)
        password_entry = tk.Entry(add_window, show="*")
        password_entry.pack(pady=5)

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack(pady=5)

        def save_user():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            email = email_entry.get().strip()

            if not username or not password or not email:
                messagebox.showerror("Error", "All fields are required.")
                return

            db = next(get_db())
            try:
                new_user = User(username=username, password=password, email=email)
                db.add(new_user)
                db.commit()
                messagebox.showinfo("Success", "User added successfully.")
                add_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(add_window, text="Save", command=save_user).pack(pady=10)

    def update_user(self):
        messagebox.showinfo("Coming Soon", "Update user functionality will be implemented.")

    def delete_user(self):
        messagebox.showinfo("Coming Soon", "Delete user functionality will be implemented.")

    def view_all_users(self):
        db = next(get_db())
        try:
            users = db.query(User).all()
            users_list = "\n".join([f"ID: {user.user_id}, Username: {user.username}, Email: {user.email}" for user in users])
            if users_list:
                messagebox.showinfo("All Users", users_list)
            else:
                messagebox.showinfo("All Users", "No users found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            db.close()
