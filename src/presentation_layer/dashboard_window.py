import tkinter as tk

class DashboardWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Dashboard")
        self.master.geometry("600x400")

        # Welcome Label
        tk.Label(master, text="Welcome, Admin!", font=("Arial", 16)).pack(pady=20)

        # Buttons for different functionalities
        tk.Button(master, text="User Management", width=20, command=self.open_user_management).pack(pady=10)
        tk.Button(master, text="Expense Management", width=20, command=self.open_expense_management).pack(pady=10)
        tk.Button(master, text="Inventory Management", width=20, command=self.open_inventory_management).pack(pady=10)
        tk.Button(master, text="Sales Tracking", width=20, command=self.open_sales_tracking).pack(pady=10)
        tk.Button(master, text="Reporting", width=20, command=self.open_reporting).pack(pady=10)

        # Back Button
        tk.Button(master, text="Back", width=20, command=self.go_back).pack(pady=10)

    def open_user_management(self):
        self.controller.show_user_management_window()

    def open_expense_management(self):
        self.controller.show_expense_management_window()

    def open_inventory_management(self):
        self.controller.show_inventory_management_window()

    def open_sales_tracking(self):
        self.controller.show_sales_tracking_window()

    def open_reporting(self):
        self.controller.show_reporting_window()

    def go_back(self):
        self.controller.show_login_window()
