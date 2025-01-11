import unittest
from src.business_logic_layer.inventory_management import add_inventory_item, view_inventory
from src.data_access_layer.database_connection import get_db, Base, engine

class TestInventoryManagement(unittest.TestCase):
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

    def test_add_inventory_item(self):
        # Test adding an inventory item
        result = add_inventory_item("Test Item", 10, 15.50)
        self.assertEqual(result, "Inventory item added successfully.")

        # Verify the item exists in the database
        session = next(get_db())
        item = session.query(Base.metadata.tables["inventory"]).filter_by(item_name="Test Item").first()
        self.assertIsNotNone(item)
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.cost, 15.50)
        session.close()

    def test_add_duplicate_inventory_item(self):
        # Add an item
        add_inventory_item("Test Item", 10, 15.50)

        # Attempt to add the same item again
        result = add_inventory_item("Test Item", 5, 10.00)
        self.assertIn("Error", result)  # Should return an error due to unique constraint

    def test_view_inventory(self):
        # Add multiple items
        add_inventory_item("Item 1", 5, 20.00)
        add_inventory_item("Item 2", 3, 30.00)

        # View inventory
        inventory = view_inventory()
        self.assertEqual(len(inventory), 2)

if __name__ == "__main__":
    unittest.main()
