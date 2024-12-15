from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///order_details.db')
Base = declarative_base()

# Create Table

class OrderDetails(Base):

    __tablename__ = "order_details"

    order_detail_id = Column(Integer, primary_key=True)
    # order_id = Foreign Key
    # menu_item_id = Foreign Key
    quantity = Column(Integer, nullable=False)
    # subtotal = quantity * price

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()

order_details1 = OrderDetails(quantity=11) # 11 Lattes / # THIS IS ALL BUSINESS LOGIC AS IT ADDS DATA TO TABLE
order_details2 = OrderDetails(quantity=7) # 7 Flat Whites

session.add_all([order_details1, order_details2])
session.commit()

session.close()