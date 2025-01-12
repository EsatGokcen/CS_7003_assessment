import tkinter as tk
from tkinter import messagebox
from src.data_access_layer.database_connection import get_db
from src.business_logic_layer.expense_management import Expense

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
        report_window = tk.Toplevel(self.master)
        report_window.title("Expense Report")
        report_window.geometry("400x300")

        tk.Label(report_window, text="Generate Expense Report").pack(pady=10)
        tk.Label(report_window, text="Enter Date Range (YYYY-MM-DD):").pack(pady=5)

        tk.Label(report_window, text="Start Date:").pack(pady=5)
        start_date_entry = tk.Entry(report_window)
        start_date_entry.pack(pady=5)

        tk.Label(report_window, text="End Date:").pack(pady=5)
        end_date_entry = tk.Entry(report_window)
        end_date_entry.pack(pady=5)

        def generate_report():
            start_date = start_date_entry.get().strip()
            end_date = end_date_entry.get().strip()

            if not start_date or not end_date:
                messagebox.showerror("Error", "Both start and end dates are required.")
                return

            db = next(get_db())
            try:
                expenses = db.query(Expense).filter(Expense.date >= start_date, Expense.date <= end_date).all()
                if not expenses:
                    messagebox.showinfo("Expense Report", "No expenses found in the given date range.")
                    return

                total_expense = sum(expense.amount for expense in expenses)
                report_lines = ["Category   | Total"]
                report_lines.append("-" * 20)
                category_totals = {}
                for expense in expenses:
                    category_totals[expense.category] = category_totals.get(expense.category, 0) + expense.amount
                for category, total in category_totals.items():
                    report_lines.append(f"{category:<10} | {total:.2f}")

                report_lines.append(f"\nTotal Expense: {total_expense:.2f}")
                report = "\n".join(report_lines)
                messagebox.showinfo("Expense Report", report)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db.close()

        tk.Button(report_window, text="Generate", command=generate_report).pack(pady=10)
        tk.Button(report_window, text="Cancel", command=report_window.destroy).pack(pady=10)

        # Make the window modal
        self.master.wait_window(report_window)

    def inventory_report(self):
        pass

    def sales_report(self):
        pass