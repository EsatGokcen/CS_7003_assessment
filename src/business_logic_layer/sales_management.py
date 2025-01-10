from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from src.data_access_layer.database_connection import Base
from src.data_access_layer.sales_table import add_sale, view_sales

class Sale(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    date = Column(String, nullable=False)  # Stored as a string in SQLite
    total_amount = Column(Float, nullable=False)

    # Optional relationship with User model
    user = relationship("User", back_populates="sales")

    def __repr__(self):
        return f"<Sale(sale_id={self.sale_id}, user_id={self.user_id}, date='{self.date}', total_amount={self.total_amount})>"


# Records a sale with validation.
def record_sale(user_id: int, date: str, total_amount: float):
    if not user_id or not date or total_amount <= 0:
        return "Error: Invalid input for user ID, date, or total amount."
    add_sale(user_id, date, total_amount)
    return "Sale recorded successfully."

# Fetches and returns all sales.
def list_sales():
    return view_sales()