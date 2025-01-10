from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from src.data_access_layer.database_connection import Base
from src.data_access_layer.expenses_table import add_expense, view_expenses

class Expense(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    date = Column(String, nullable=False)  # Stored as string in SQLite
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationship with User model (optional)
    user = relationship("User", back_populates="expenses", lazy="joined")

    def __repr__(self):
        return f"<Expense(expense_id={self.expense_id}, user_id={self.user_id}, date='{self.date}', amount={self.amount}, category='{self.category}')>"


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