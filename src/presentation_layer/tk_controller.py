import tkinter as tk

from src.presentation_layer.dashboard_window import DashboardWindow
from src.presentation_layer.expense_management_window import ExpenseManagementWindow
from src.presentation_layer.inventory_management_window import InventoryManagementWindow
from src.presentation_layer.login_window import LoginWindow
from src.presentation_layer.sales_tracking_window import SalesTrackingWindow
from src.presentation_layer.user_management_window import UserManagementWindow


class TkController:
    def __init__(self):
        self.root = tk.Tk()

    def start(self):
        self.show_login_window()
        self.root.mainloop()

    def show_login_window(self):
        self.clear_window()
        LoginWindow(self.root, self)

    def show_dashboard_window(self):
        self.clear_window()
        DashboardWindow(self.root, self)

    def show_user_management_window(self):
        self.clear_window()
        UserManagementWindow(self.root, self)

    def show_expense_management_window(self):
        self.clear_window()
        ExpenseManagementWindow(self.root, self)

    def show_inventory_management_window(self):
        self.clear_window()
        InventoryManagementWindow(self.root, self)

    def show_sales_tracking_window(self):
        self.clear_window()
        SalesTrackingWindow(self.root, self)

    def show_reporting_window(self):
        self.clear_window()
        # Logic

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
