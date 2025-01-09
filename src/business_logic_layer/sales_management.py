from src.data_access_layer.sales_table import add_sale, view_sales

# Records a sale with validation.
def record_sale(user_id: int, date: str, total_amount: float):
    if not user_id or not date or total_amount <= 0:
        return "Error: Invalid input for user ID, date, or total amount."
    add_sale(user_id, date, total_amount)
    return "Sale recorded successfully."

# Fetches and returns all sales.
def list_sales():
    return view_sales()