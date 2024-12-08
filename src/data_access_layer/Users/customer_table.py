from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///customer.db')
Base = declarative_base()

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)

