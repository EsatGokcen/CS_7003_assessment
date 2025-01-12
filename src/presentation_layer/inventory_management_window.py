import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.inventory_management import InventoryItem

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

    def add_inventory_item(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Inventory Item")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Item Name:").pack(pady=5)
        item_name_entry = tk.Entry(add_window)
        item_name_entry.pack(pady=5)

        tk.Label(add_window, text="Quantity:").pack(pady=5)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack(pady=5)

        tk.Label(add_window, text="Cost:").pack(pady=5)
        cost_entry = tk.Entry(add_window)
        cost_entry.pack(pady=5)

        def save_item():
            item_name = item_name_entry.get().strip()
            quantity = quantity_entry.get().strip()
            cost = cost_entry.get().strip()

            if not item_name or not quantity or not cost:
                messagebox.showerror("Error", "All fields are required.")
                return

            db = next(get_db())
            try:
                new_item = InventoryItem(item_name=item_name, quantity=int(quantity), cost=float(cost))
                db.add(new_item)
                db.commit()
                messagebox.showinfo("Success", "Inventory item added successfully.")
                add_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(add_window, text="Save", command=save_item).pack(pady=10)

        # Make the window modal
        self.master.wait_window(add_window)

    def update_inventory_item(self):
        pass

    def delete_inventory_item(self):
        pass

    def view_inventory(self):
        pass