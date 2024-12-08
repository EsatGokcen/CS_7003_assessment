from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///employee_roles.db')
Base = declarative_base()

class Roles(Base):

    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String)
