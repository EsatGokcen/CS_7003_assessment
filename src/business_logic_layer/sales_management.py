from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from datetime import datetime
from src.data_access_layer.database_connection import Base, get_db
from src.data_access_layer.sales_table import add_sale, view_sales
from src.business_logic_layer.user_management import User

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
def record_sale(user_id: int, date: str, total_amount: float) -> str:
    session: Session = next(get_db())
    try:
        # Validate the user exists
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return f"Error: User with ID {user_id} does not exist."

        # Add the sale record
        new_sale = Sale(user_id=user_id, date=date, total_amount=total_amount)
        session.add(new_sale)
        session.commit()
        return "Sale recorded successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()


# Fetches and returns all sales.
def list_sales():
    return view_sales()