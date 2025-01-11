import unittest
from src.business_logic_layer.sales_management import record_sale, calculate_revenue, view_sales_history, delete_sale
from src.business_logic_layer.user_management import register_user
from src.data_access_layer.database_connection import get_db, Base, engine
from datetime import datetime

class TestSalesManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create tables in a temporary SQLite database for testing
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        # Drop all tables after tests
        Base.metadata.drop_all(bind=engine)

    # Start a new session for each test.
    def setUp(self):
        self.db = next(get_db())  # Advance the generator to get the session

    # Close the session after each test.
    def tearDown(self):
        self.db.close()

        # Create a test user
        register_user("testuser", "password123", "test@example.com", False)

    def test_record_sale(self):
        # Record a sale
        date = datetime.now().strftime("%Y-%m-%d")
        result = record_sale(1, date, 100.0)
        self.assertEqual(result, "Sale recorded successfully.")

        # Verify the sale exists
        sales = view_sales_history()
        self.assertEqual(len(sales), 1)
        self.assertEqual(sales[0].total_amount, 100.0)

    def test_calculate_revenue(self):
        # Record multiple sales
        date = datetime.now().strftime("%Y-%m-%d")
        record_sale(1, date, 100.0)
        record_sale(1, date, 200.0)

        # Calculate revenue
        revenue = calculate_revenue()
        self.assertEqual(revenue, 300.0)

if __name__ == "__main__":
    unittest.main()
