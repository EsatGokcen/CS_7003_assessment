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

        # Make the window modal
        self.master.wait_window(add_window)

    def update_user(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update User")
        update_window.geometry("400x400")

        # User ID selection
        tk.Label(update_window, text="User ID to Update:").pack(pady=5)
        user_id_entry = tk.Entry(update_window)
        user_id_entry.pack(pady=5)

        # New username
        tk.Label(update_window, text="New Username (leave blank to keep unchanged):").pack(pady=5)
        new_username_entry = tk.Entry(update_window)
        new_username_entry.pack(pady=5)

        # New password
        tk.Label(update_window, text="New Password (leave blank to keep unchanged):").pack(pady=5)
        new_password_entry = tk.Entry(update_window, show="*")
        new_password_entry.pack(pady=5)

        # New email
        tk.Label(update_window, text="New Email (leave blank to keep unchanged):").pack(pady=5)
        new_email_entry = tk.Entry(update_window)
        new_email_entry.pack(pady=5)

        def save_update():
            user_id = user_id_entry.get().strip()
            new_username = new_username_entry.get().strip()
            new_password = new_password_entry.get().strip()
            new_email = new_email_entry.get().strip()

            if not user_id:
                messagebox.showerror("Error", "User ID is required.")
                return

            db = next(get_db())
            try:
                # Fetch the user to update
                user = db.query(User).filter_by(user_id=user_id).first()
                if not user:
                    messagebox.showerror("Error", "User not found.")
                    return

                # Update user details if provided
                if new_username:
                    user.username = new_username
                if new_password:
                    user.password = new_password
                if new_email:
                    user.email = new_email

                db.commit()
                messagebox.showinfo("Success", "User updated successfully.")
                update_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(update_window, text="Save Changes", command=save_update).pack(pady=20)

        # Make the window modal
        self.master.wait_window(update_window)

    def delete_user(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete User")
        delete_window.geometry("400x200")

        # User ID entry
        tk.Label(delete_window, text="User ID to Delete:").pack(pady=10)
        user_id_entry = tk.Entry(delete_window)
        user_id_entry.pack(pady=10)

        def confirm_delete():
            user_id = user_id_entry.get().strip()

            if not user_id:
                messagebox.showerror("Error", "User ID is required.")
                return

            db = next(get_db())
            try:
                # Fetch the user to delete
                user = db.query(User).filter_by(user_id=user_id).first()
                if not user:
                    messagebox.showerror("Error", "User not found.")
                    return

                # Delete the user
                db.delete(user)
                db.commit()
                messagebox.showinfo("Success", f"User with ID {user_id} deleted successfully.")
                delete_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        # Buttons
        tk.Button(delete_window, text="Delete User", command=confirm_delete).pack(pady=10)
        tk.Button(delete_window, text="Cancel", command=delete_window.destroy).pack(pady=10)

        # Make the window modal
        self.master.wait_window(delete_window)

    def view_all_users(self):
        db = next(get_db())
        try:
            users = db.query(User).all()
            if not users:
                messagebox.showinfo("All Users", "No users found.")
                return

            # Build the report
            report_lines = ["ID | Username       | Email"]
            report_lines.append("-" * 30)  # Separator line
            for user in users:
                report_lines.append(f"{user.user_id:<3} | {user.username:<14} | {user.email}")

            # Join the report lines with newlines
            report = "\n".join(report_lines)

            # Show the report in a messagebox
            messagebox.showinfo("All Users", report)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            db.close()

