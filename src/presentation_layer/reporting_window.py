import tkinter as tk

class ReportingWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Reporting")
        self.master.geometry("600x400")

        # Title
        tk.Label(master, text="Reporting", font=("Arial", 16)).pack(pady=10)

        # Buttons for different report types
        tk.Button(master, text="Expense Report", width=20, command=self.expense_report).pack(pady=5)
        tk.Button(master, text="Inventory Report", width=20, command=self.inventory_report).pack(pady=5)
        tk.Button(master, text="Sales Report", width=20, command=self.sales_report).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back to Dashboard", width=20, command=self.controller.show_dashboard_window).pack(pady=20)

    def expense_report(self):
        pass

    def inventory_report(self):
        pass

    def sales_report(self):
        pass