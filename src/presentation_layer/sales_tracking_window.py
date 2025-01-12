import tkinter as tk

class SalesTrackingWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Sales Tracking")
        self.master.geometry("600x400")

        # Title
        tk.Label(master, text="Sales Tracking", font=("Arial", 16)).pack(pady=10)

        # Buttons for different sales tracking functionalities
        tk.Button(master, text="Record New Sale", width=20, command=self.record_sale).pack(pady=5)
        tk.Button(master, text="View All Sales", width=20, command=self.view_all_sales).pack(pady=5)
        tk.Button(master, text="View Sales by Date", width=20, command=self.view_sales_by_date).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back to Dashboard", width=20, command=self.controller.show_dashboard_window).pack(pady=20)

    def record_sale(self):
        pass

    def view_all_sales(self):
        pass

    def view_sales_by_date(self):
        pass