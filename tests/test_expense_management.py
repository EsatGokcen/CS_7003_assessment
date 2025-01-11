import unittest
from src.business_logic_layer.expense_management import view_expenses, view_expenses_by_category, delete_expense


class TestExpenseManagement(unittest.TestCase):
    # Test viewing all expenses.
    def test_view_expenses(self):
        expenses = view_expenses()
        # Mock data includes 5 expenses as defined in populate_mock_data
        self.assertEqual(len(expenses), 4)
        # Verify specific details of one expense
        self.assertEqual(expenses[0].description, "Monthly shop rent")
        self.assertEqual(expenses[0].amount, 1500.00)

    # Test viewing expenses by category.
    def test_view_expenses_by_category(self):
        # Verify the "Rent" category contains 1 expense
        rent_expenses = view_expenses_by_category("Rent")
        self.assertEqual(len(rent_expenses), 1)
        self.assertEqual(rent_expenses[0].description, "Monthly shop rent")
        self.assertEqual(rent_expenses[0].amount, 1500.00)

        # Verify the "Stock" category contains 1 expense
        stock_expenses = view_expenses_by_category("Stock")
        self.assertEqual(len(stock_expenses), 1)
        self.assertEqual(stock_expenses[0].description, "Coffee beans and milk")
        self.assertEqual(stock_expenses[0].amount, 600.00)

    # Test deleting an expense.
    def test_delete_expense(self):
        # Mock data includes an expense with user_id=2 and date="2025-01-01"
        expenses = view_expenses()
        expense_id = expenses[0].expense_id  # Pick the first expense
        result = delete_expense(expense_id=expense_id)
        self.assertEqual(result, f"Expense with ID {expense_id} deleted successfully.")

        # Verify the expense count decreases
        updated_expenses = view_expenses()
        self.assertEqual(len(updated_expenses), 4)  # One expense was removed

        # Ensure the deleted expense is no longer present
        remaining_ids = [expense.expense_id for expense in updated_expenses]
        self.assertNotIn(expense_id, remaining_ids)


if __name__ == "__main__":
    unittest.main()
