from src.data_access_layer.inventory_table import add_item, view_inventory, view_item_in_inventory, delete_item

# Adds an inventory item with validation.
def add_item_to_inventory(item_name: str, quantity: int, cost: float) -> str:
    if not item_name or quantity <= 0 or cost <= 0:
        return "Error: Invalid input for item name, quantity, or cost."
    add_item(item_name, quantity, cost)
    return "Item added to inventory successfully."

# Fetches and returns all inventory items.
def list_inventory():
    return view_inventory()

# Fetches and returns a specific inventory item.
def list_item_in_inventory(item_name: str):
    return view_item_in_inventory(item_name)

# Deletes an item based on the ID.
def remove_item(item_id: int):
    return delete_item(item_id)