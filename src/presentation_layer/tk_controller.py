import tkinter as tk

from src.presentation_layer.login_window import LoginWindow


class TkController:
    def __init__(self):
        self.root = tk.Tk()

    def start(self):
        self.show_login_window()
        self.root.mainloop()

    def show_login_window(self):
        self.clear_window()
        LoginWindow(self.root, self)

    def show_user_management_window(self):
        self.clear_window()
        # Logic

    def show_expense_management_window(self):
        self.clear_window()
        # Logic

    def show_inventory_management_window(self):
        self.clear_window()
        # Logic

    def show_sales_tracking_window(self):
        self.clear_window()
        # Logic

    def show_reporting_window(self):
        self.clear_window()
        # Logic

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
