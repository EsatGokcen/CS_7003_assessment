import tkinter as tk

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
        pass

    def view_all_expenses(self):
        pass

    def view_expenses_by_category(self):
        pass