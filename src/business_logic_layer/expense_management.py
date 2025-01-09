from src.data_access_layer.expenses_table import add_expense, view_expenses

# Adds an expense entry with validation.
def add_expense_entry(user_id: int, date: str, amount: float, category: str, description: str) -> str:
    if not user_id or not date or not amount or not category:
        return "Error: All fields except description are required."
    if amount <= 0:
        return "Error: Expense amount must be positive."
    add_expense(user_id, date, amount, category, description)
    return "Expense recorded successfully."

# Fetches and returns all expenses.
def list_expenses():
    return view_expenses()