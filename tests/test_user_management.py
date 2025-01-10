import unittest
from src.business_logic_layer.user_management import register_user, update_user, remove_user, list_users
from src.data_access_layer.database_connection import get_db, Base, engine

class TestUserManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create tables in a temporary SQLite database for testing
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        # Drop all tables after tests
        Base.metadata.drop_all(bind=engine)

    def setUp(self):
        # Clear all tables before each test
        session = next(get_db())
        for table in Base.metadata.tables.values():
            session.execute(table.delete())
        session.commit()
        session.close()

    def test_register_user(self):
        # Test registering a user
        result = register_user("testuser", "password123", "test@example.com", False)
        self.assertEqual(result, "User registered successfully.")

        # Verify the user exists in the database
        users = list_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "testuser")

    def test_register_duplicate_user(self):
        # Add a user
        register_user("testuser", "password123", "test@example.com", False)

        # Attempt to add the same user again
        result = register_user("testuser", "password123", "test@example.com", False)
        self.assertIn("Error", result)  # Should return an error due to unique constraint

    def test_update_user(self):
        # Add a user
        register_user("testuser", "password123", "test@example.com", False)

        # Update the user's email and password
        result = update_user(1, username="updateduser", password="newpassword", email="updated@example.com")
        self.assertEqual(result, "User with ID 1 updated successfully.")

        # Verify the user was updated
        users = list_users()
        self.assertEqual(users[0].username, "updateduser")
        self.assertEqual(users[0].email, "updated@example.com")

    def test_remove_user(self):
        # Add a user
        register_user("testuser", "password123", "test@example.com", False)

        # Remove the user
        result = remove_user(1)
        self.assertEqual(result, "User with ID 1 deleted successfully.")

        # Verify the user was deleted
        users = list_users()
        self.assertEqual(len(users), 0)

if __name__ == "__main__":
    unittest.main()
