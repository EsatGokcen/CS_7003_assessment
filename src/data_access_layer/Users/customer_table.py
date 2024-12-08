from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///customer.db')
Base = declarative_base()

# Create Table

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

customer1 = Customer(name='Esra Gokcen', email='esrag@mail.com', password='gok123')
customer2 = Customer(name='Eda Gokcen', email='edagokcen@hotmail.com', password='Pirtik24!')

session.add_all([])
session.commit()

session.close()

