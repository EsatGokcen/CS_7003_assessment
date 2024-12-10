from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///categories.db')
Base = declarative_base()

# Create Table

class Categories(Base):

    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)

Base.metadata.create_all(engine)