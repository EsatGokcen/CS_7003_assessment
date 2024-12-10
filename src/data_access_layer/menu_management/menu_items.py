from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///menu_items.db')
Base = declarative_base()

# Create Table

class MenuItems(Base):

    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)
    IsAvailable = Column(Boolean)

Base.metadata.create_all(engine)