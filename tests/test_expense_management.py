import unittest
from src.business_logic_layer.expense_management import record_expense, view_expenses, view_expenses_by_category, delete_expense
from src.data_access_layer.database_connection import Base, engine, get_db
from sqlalchemy.orm import sessionmaker

class TestExpenseManagement(unittest.TestCase):
    # Set up the database schema.
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    # Drop the database schema.
    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)

    # Start a new session for each test.
    def setUp(self):
        self.db = next(get_db())  # Advance the generator to get the session

    # Close the session after each test.
    def tearDown(self):
        self.db.close()

    # Test recording an expense.
    def test_record_expense(self):
        result = record_expense(user_id=1, date="2025-01-10", amount=100.0, category="Food", description="Lunch")
        self.assertEqual(result, "Expense recorded successfully.")

    # Test viewing all expenses.
    def test_view_expenses(self):
        record_expense(user_id=1, date="2025-01-10", amount=100.0, category="Food", description="Lunch")
        record_expense(user_id=1, date="2025-01-11", amount=50.0, category="Travel", description="Taxi")
        expenses = view_expenses()
        self.assertEqual(len(expenses), 2)

    # Test viewing expenses by category.
    def test_view_expenses_by_category(self):
        record_expense(user_id=1, date="2025-01-10", amount=100.0, category="Food", description="Lunch")
        record_expense(user_id=1, date="2025-01-11", amount=50.0, category="Travel", description="Taxi")
        food_expenses = view_expenses_by_category("Food")
        self.assertEqual(len(food_expenses), 1)
        self.assertEqual(food_expenses[0].category, "Food")

    # Test deleting an expense.
    def test_delete_expense(self):
        record_expense(user_id=1, date="2025-01-10", amount=100.0, category="Food", description="Lunch")
        expense = view_expenses()[0]
        result = delete_expense(expense_id=expense.expense_id)
        self.assertEqual(result, f"Expense with ID {expense.expense_id} deleted successfully.")
        self.assertEqual(len(view_expenses()), 0)

if __name__ == "__main__":
    unittest.main()
