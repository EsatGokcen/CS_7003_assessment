from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from src.data_access_layer.database_connection import Base, get_db
from src.business_logic_layer.user_management import User

class Sale(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    date = Column(String, nullable=False)  # Stored as a string in SQLite
    total_amount = Column(Float, nullable=False)

    # Relationship with User model
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

def calculate_revenue(start_date: str = None, end_date: str = None) -> float:
    session: Session = next(get_db())
    try:
        query = session.query(Sale)

        # Filter by date range if provided
        if start_date:
            query = query.filter(Sale.date >= start_date)
        if end_date:
            query = query.filter(Sale.date <= end_date)

        # Sum up total_amount from the query
        total_revenue = sum(sale.total_amount for sale in query.all())
        return total_revenue
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        session.close()

def view_sales_history(start_date: str = None, end_date: str = None):
    session: Session = next(get_db())
    try:
        query = session.query(Sale)

        # Filter by date range if provided
        if start_date:
            query = query.filter(Sale.date >= start_date)
        if end_date:
            query = query.filter(Sale.date <= end_date)

        # Fetch and return results
        sales = query.all()
        return sales
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        session.close()

def delete_sale(sale_id: int) -> str:
    session: Session = next(get_db())
    try:
        sale = session.query(Sale).filter(Sale.sale_id == sale_id).first()
        if not sale:
            return f"Error: Sale with ID {sale_id} does not exist."

        session.delete(sale)
        session.commit()
        return f"Sale with ID {sale_id} deleted successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()
