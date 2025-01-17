from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import Session
from src.data_access_layer.database_connection import Base, get_db

class InventoryItem(Base):
    __tablename__ = "inventory"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

    def __repr__(self):
        return f"<InventoryItem(item_id={self.item_id}, item_name='{self.item_name}', quantity={self.quantity}, cost={self.cost})>"

def add_inventory_item(item_name: str, quantity: int, cost: float) -> str:
    session: Session = next(get_db())
    try:
        # Add the inventory item
        new_item = InventoryItem(item_name=item_name, quantity=quantity, cost=cost)
        session.add(new_item)
        session.commit()
        return "Inventory item added successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()

def view_inventory():
    session: Session = next(get_db())
    try:
        inventory = session.query(InventoryItem).all()
        return inventory
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        session.close()

def update_inventory_item(item_id: int, quantity: int = None, cost: float = None) -> str:
    session: Session = next(get_db())
    try:
        item = session.query(InventoryItem).filter(InventoryItem.item_id == item_id).first()
        if not item:
            return f"Error: Item with ID {item_id} does not exist."

        if quantity is not None:
            item.quantity = quantity
        if cost is not None:
            item.cost = cost

        session.commit()
        return f"Inventory item with ID {item_id} updated successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()

def delete_inventory_item(item_id: int) -> str:
    session: Session = next(get_db())
    try:
        item = session.query(InventoryItem).filter(InventoryItem.item_id == item_id).first()
        if not item:
            return f"Error: Item with ID {item_id} does not exist."

        session.delete(item)
        session.commit()
        return f"Item with ID {item_id} deleted successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()
