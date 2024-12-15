from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///inventory_audit.db')
Base = declarative_base()

# Create Table

class InventoryAudit(Base):

    __tablename__ = "inventory_audit"

    audit_id = Column(Integer, primary_key=True)
    # inventory_id = Foreign Key
    action = Column(String) # restocked, used etc.
    old_quantity = Column(Integer, nullable=False)
    new_quantity = Column(Integer, nullable=False)
    time_stamp = Column(String)

Base.metadata.create_all(engine)