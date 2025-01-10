from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from src.data_access_layer.database_connection import Base, get_db
from src.business_logic_layer.user_management import User

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

def record_expense(user_id: int, date: str, amount: float, category: str, description: str = None) -> str:
    session: Session = next(get_db())
    try:
        # Validate user exists
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return f"Error: User with ID {user_id} does not exist."

        # Record the expense
        new_expense = Expense(user_id=user_id, date=date, amount=amount, category=category, description=description)
        session.add(new_expense)
        session.commit()
        return "Expense recorded successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()
