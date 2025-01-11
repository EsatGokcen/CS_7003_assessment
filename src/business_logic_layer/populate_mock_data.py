from src.data_access_layer.database_connection import Base, engine, get_db
from src.business_logic_layer.user_management import User
from src.business_logic_layer.expense_management import Expense
from src.business_logic_layer.inventory_management import InventoryItem
from src.business_logic_layer.sales_management import Sale

def populate_users(session):
    users = [
        User(username="john_doe", password="password123", email="john.doe@example.com", is_admin=False),
        User(username="jane_smith", password="password456", email="jane.smith@example.com", is_admin=True),
        User(username="alice_brown", password="password789", email="alice.brown@example.com", is_admin=False),
    ]
    for user in users:
        if not session.query(User).filter_by(email=user.email).first():
            session.add(user)

def populate_expenses(session):
    expenses = [
        Expense(user_id=2, date="2025-01-01", amount=1500.00, category="Rent", description="Monthly shop rent"),
        Expense(user_id=2, date="2025-01-02", amount=500.00, category="Utilities", description="Electricity and water bills"),
        Expense(user_id=2, date="2025-01-03", amount=2500.00, category="Wages", description="Monthly staff wages"),
        Expense(user_id=2, date="2025-01-05", amount=600.00, category="Stock", description="Coffee beans and milk"),
        Expense(user_id=2, date="2025-01-07", amount=300.00, category="Marketing", description="Social media advertising"),
    ]
    for expense in expenses:
        if not session.query(Expense).filter_by(date=expense.date, user_id=expense.user_id).first():
            session.add(expense)

def populate_inventory(session):
    inventory = [
        InventoryItem(item_name="Coffee Beans", quantity=50, cost=25.0),
        InventoryItem(item_name="Milk", quantity=20, cost=15.0),
        InventoryItem(item_name="Pastries", quantity=100, cost=30.0),
    ]
    for item in inventory:
        if not session.query(InventoryItem).filter_by(item_name=item.item_name).first():
            session.add(item)

def populate_sales(session):
    sales = [
        Sale(user_id=1, date="2025-01-04", total_amount=75.00),
        Sale(user_id=2, date="2025-01-05", total_amount=200.00),
        Sale(user_id=3, date="2025-01-06", total_amount=150.00),
    ]
    for sale in sales:
        if not session.query(Sale).filter_by(date=sale.date, user_id=sale.user_id).first():
            session.add(sale)

# Populates the database with mock data.
def populate_mock_data():
    db = next(get_db())  # Use the get_db() function to get a session
    try:
        populate_users(db)
        populate_expenses(db)
        populate_inventory(db)
        populate_sales(db)
        db.commit()
        print("Mock data populated successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error occurred while populating mock data: {e}")
    finally:
        db.close()