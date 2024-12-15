from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///orders.db')
Base = declarative_base()

# Create Table

class Orders(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    # customer_id = Foreign Key
    # employee_id = Foreign Key
    order_date = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

order1 = Orders(order_date="10/12/2024", total_amount=34.65) # 11 Lattes / # THIS IS ALL BUSINESS LOGIC AS IT ADDS DATA TO TABLE
order2 = Orders(order_date="27/11/2024", total_amount=24.15) # 7 Flat Whites

session.add_all([order1, order2])
session.commit()

session.close()