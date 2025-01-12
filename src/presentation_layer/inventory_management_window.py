import tkinter as tk

class InventoryManagementWindow:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Inventory Management")
        self.master.geometry("600x400")

        # Title
        tk.Label(master, text="Inventory Management", font=("Arial", 16)).pack(pady=10)

        # Buttons for different inventory management functionalities
        tk.Button(master, text="Add Inventory Item", width=20, command=self.add_inventory_item).pack(pady=5)
        tk.Button(master, text="Update Inventory Item", width=20, command=self.update_inventory_item).pack(pady=5)
        tk.Button(master, text="Delete Inventory Item", width=20, command=self.delete_inventory_item).pack(pady=5)
        tk.Button(master, text="View All Inventory Items", width=20, command=self.view_inventory).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back to Dashboard", width=20, command=self.controller.show_dashboard_window).pack(pady=20)