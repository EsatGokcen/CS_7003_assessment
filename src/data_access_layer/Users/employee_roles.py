from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///employee_roles.db')
Base = declarative_base()

# Create table

class Roles(Base):

    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

role1 = Roles(role_name='Manager')
role2 = Roles(role_name='Barista')

session.add_all([role1, role2])
session.commit()

session.close()
