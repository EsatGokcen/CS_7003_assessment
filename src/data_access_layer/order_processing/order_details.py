from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///order_details.db')
Base = declarative_base()

# Create Table

class OrderDetails(Base):

    __tablename__ = "order_details"

    order_detail_id = Column(Integer, primary_key=True)
    # order_id = Foreign Key
    # menu_item_id = Foreign Key
    quantity = Column(Integer, nullable=False)
    # subtotal = quantity * price

Base.metadata.create_all(engine)