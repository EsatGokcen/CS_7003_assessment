import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.expense_management import Expense

class ExpenseManagementWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Expense Management")
        self.master.geometry("600x400")

        # Title
        tk.Label(master, text="Expense Management", font=("Arial", 16)).pack(pady=10)

        # Buttons for different expense management functionalities
        tk.Button(master, text="Add Expense", width=20, command=self.add_expense).pack(pady=5)
        tk.Button(master, text="View All Expenses", width=20, command=self.view_all_expenses).pack(pady=5)
        tk.Button(master, text="View Expenses by Category", width=20, command=self.view_expenses_by_category).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back to Dashboard", width=20, command=self.controller.show_dashboard_window).pack(pady=20)

    def add_expense(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Expense")
        add_window.geometry("400x400")

        # Input fields for expense details
        tk.Label(add_window, text="User ID:").pack(pady=5)
        user_id_entry = tk.Entry(add_window)
        user_id_entry.pack(pady=5)

        tk.Label(add_window, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.pack(pady=5)

        tk.Label(add_window, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(add_window)
        amount_entry.pack(pady=5)

        tk.Label(add_window, text="Category:").pack(pady=5)
        category_entry = tk.Entry(add_window)
        category_entry.pack(pady=5)

        tk.Label(add_window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack(pady=5)

        def save_expense():
            user_id = user_id_entry.get().strip()
            date = date_entry.get().strip()
            amount = amount_entry.get().strip()
            category = category_entry.get().strip()
            description = description_entry.get().strip()

            if not user_id or not date or not amount or not category:
                messagebox.showerror("Error", "All fields except description are required.")
                return

            db = next(get_db())
            try:
                new_expense = Expense(user_id=user_id, date=date, amount=float(amount), category=category,
                                      description=description)
                db.add(new_expense)
                db.commit()
                messagebox.showinfo("Success", "Expense added successfully.")
                add_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(add_window, text="Save", command=save_expense).pack(pady=10)

        # Make the window modal
        self.master.wait_window(add_window)

    def view_all_expenses(self):
        pass

    def view_expenses_by_category(self):
        pass