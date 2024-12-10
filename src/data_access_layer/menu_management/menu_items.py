from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///menu_items.db')
Base = declarative_base()

# Create Table

class MenuItems(Base):

    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    IsAvailable = Column(Boolean)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

item1 = MenuItems(name="Latte", price=3.15, description="single shot milk coffee", IsAvailable=True)
item2 = MenuItems(name="Flat White", price=3.45, description="double shot milk froth coffee", IsAvailable=True)

session.add_all([item1, item2])
session.commit()

session.close()