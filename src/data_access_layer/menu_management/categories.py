from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///categories.db') # KEEP EVERYTHING IN ONE DATABASE
Base = declarative_base() # IMPORT BASE FOR EACH FILE AND ONLY CALL FUNCTION ONCE

# Create Table

class Categories(Base):

    __tablename__ = "categories" # NEED TO USE SQLITE

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

category1 = Categories(category_name="Beverages") # THIS IS ALL BUSINESS LOGIC AS IT ADDS DATA TO TABLE
category2 = Categories(category_name="Utensils")

session.add_all([category1, category2])
session.commit()

session.close()