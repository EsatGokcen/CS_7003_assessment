from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///inventory.db')
Base = declarative_base()

# Create Table

class Inventory(Base):

    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    # unit_id = Foreign Key
    quantity = Column(Integer, nullable=False)
    cost_price = Column(Float, nullable=False)

Base.metadata.create_all(engine)