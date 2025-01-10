from sqlalchemy import Column, Integer, Float, String
from src.data_access_layer.database_connection import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

    def __repr__(self):
        return f"<InventoryItem(item_id={self.item_id}, item_name='{self.item_name}', quantity={self.quantity}, cost={self.cost})>"
