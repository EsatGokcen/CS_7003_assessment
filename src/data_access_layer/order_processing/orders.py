from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///orders.db')
Base = declarative_base()

# Create Table

class Orders(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    # customer_id = Foreign Key
    # employee_id = Foreign Key
    order_date = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)

Base.metadata.create_all(engine)