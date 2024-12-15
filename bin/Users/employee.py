from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///employee.db')
Base = declarative_base()

# Create table

class Employee(Base):

    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    salary = Column(Integer)

Base.metadata.create_all(engine)

# Create session and add data to table

Session = sessionmaker(bind=engine)
session = Session()
# THIS IS ALL BUSINESS LOGIC AS IT ADDS DATA TO TABLE
employee1 = Employee(name='Esat Gokcen', email='esatgokcen@gmail.com', password='KingSnake31!', salary=40000)
employee2 = Employee(name='Taha Tariq', email='taha@hotmail.com', password='TahaisBest!', salary=30000)

session.add_all([employee1, employee2])
session.commit()

session.close()