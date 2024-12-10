from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///units.db')
Base = declarative_base()

# Create Table

class Units(Base):

    __tablename__ = "units"

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(String, nullable=False)

Base.metadata.create_all(engine)