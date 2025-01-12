import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.sales_management import Sale

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
        record_window = tk.Toplevel(self.master)
        record_window.title("Record New Sale")
        record_window.geometry("400x300")

        tk.Label(record_window, text="User ID:").pack(pady=5)
        user_id_entry = tk.Entry(record_window)
        user_id_entry.pack(pady=5)

        tk.Label(record_window, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(record_window)
        date_entry.pack(pady=5)

        tk.Label(record_window, text="Total Amount:").pack(pady=5)
        total_amount_entry = tk.Entry(record_window)
        total_amount_entry.pack(pady=5)

        def save_sale():
            user_id = user_id_entry.get().strip()
            date = date_entry.get().strip()
            total_amount = total_amount_entry.get().strip()

            if not user_id or not date or not total_amount:
                messagebox.showerror("Error", "All fields are required.")
                return

            db = next(get_db())
            try:
                new_sale = Sale(user_id=user_id, date=date, total_amount=float(total_amount))
                db.add(new_sale)
                db.commit()
                messagebox.showinfo("Success", "Sale recorded successfully.")
                record_window.destroy()
            except Exception as e:
                db.rollback()
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(record_window, text="Save", command=save_sale).pack(pady=10)

        # Make the window modal
        self.master.wait_window(record_window)

    def view_all_sales(self):
        db = next(get_db())
        try:
            sales = db.query(Sale).all()
            if not sales:
                messagebox.showinfo("Sales", "No sales records found.")
                return

            report_lines = ["ID | User ID | Date       | Total Amount"]
            report_lines.append("-" * 40)
            for sale in sales:
                report_lines.append(
                    f"{sale.sale_id:<3} | {sale.user_id:<7} | {sale.date:<10} | {sale.total_amount:<12.2f}")

            report = "\n".join(report_lines)
            messagebox.showinfo("All Sales", report)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            db.close()

    def view_sales_by_date(self):
        date_window = tk.Toplevel(self.master)
        date_window.title("View Sales by Date")
        date_window.geometry("400x200")

        tk.Label(date_window, text="Enter Date (YYYY-MM-DD):").pack(pady=10)
        date_entry = tk.Entry(date_window)
        date_entry.pack(pady=10)

        def filter_sales():
            date = date_entry.get().strip()
            if not date:
                messagebox.showerror("Error", "Date is required.")
                return

            db = next(get_db())
            try:
                sales = db.query(Sale).filter_by(date=date).all()
                if not sales:
                    messagebox.showinfo("Sales", f"No sales found for date '{date}'.")
                    return

                report_lines = ["ID | User ID | Total Amount"]
                report_lines.append("-" * 30)
                for sale in sales:
                    report_lines.append(f"{sale.sale_id:<3} | {sale.user_id:<7} | {sale.total_amount:<12.2f}")

                report = "\n".join(report_lines)
                messagebox.showinfo(f"Sales on {date}", report)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(date_window, text="Filter", command=filter_sales).pack(pady=10)
        tk.Button(date_window, text="Cancel", command=date_window.destroy).pack(pady=10)

        # Make the window modal
        self.master.wait_window(date_window)