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
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Inventory Item")
        update_window.geometry("400x400")

        tk.Label(update_window, text="Item ID to Update:").pack(pady=5)
        item_id_entry = tk.Entry(update_window)
        item_id_entry.pack(pady=5)

        tk.Label(update_window, text="New Quantity (leave blank to keep unchanged):").pack(pady=5)
        new_quantity_entry = tk.Entry(update_window)
        new_quantity_entry.pack(pady=5)

        tk.Label(update_window, text="New Cost (leave blank to keep unchanged):").pack(pady=5)
        new_cost_entry = tk.Entry(update_window)
        new_cost_entry.pack(pady=5)

        def save_update():
            item_id = item_id_entry.get().strip()
            new_quantity = new_quantity_entry.get().strip()
            new_cost = new_cost_entry.get().strip()

            if not item_id:
                messagebox.showerror("Error", "Item ID is required.")
                return

            db = next(get_db())
            try:
                item = db.query(InventoryItem).filter_by(item_id=item_id).first()
                if not item:
                    messagebox.showerror("Error", "Item not found.")
                    return

                if new_quantity:
                    item.quantity = int(new_quantity)
                if new_cost:
                    item.cost = float(new_cost)

                db.commit()
                messagebox.showinfo("Success", "Inventory item updated successfully.")
                update_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(update_window, text="Save Changes", command=save_update).pack(pady=10)

        # Make the window modal
        self.master.wait_window(update_window)

    def delete_inventory_item(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Inventory Item")
        delete_window.geometry("400x200")

        tk.Label(delete_window, text="Item ID to Delete:").pack(pady=10)
        item_id_entry = tk.Entry(delete_window)
        item_id_entry.pack(pady=10)

        def confirm_delete():
            item_id = item_id_entry.get().strip()

            if not item_id:
                messagebox.showerror("Error", "Item ID is required.")
                return

            db = next(get_db())
            try:
                item = db.query(InventoryItem).filter_by(item_id=item_id).first()
                if not item:
                    messagebox.showerror("Error", "Item not found.")
                    return

                db.delete(item)
                db.commit()
                messagebox.showinfo("Success", f"Item with ID {item_id} deleted successfully.")
                delete_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(delete_window, text="Delete Item", command=confirm_delete).pack(pady=10)
        tk.Button(delete_window, text="Cancel", command=delete_window.destroy).pack(pady=10)

        # Make the window modal
        self.master.wait_window(delete_window)

    def view_inventory(self):
        pass