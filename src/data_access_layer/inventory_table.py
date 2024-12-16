import sqlite3
from src.data_access_layer.database_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

def create_inventory_table():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT UNIQUE NOT NULL,
        quantity INTEGER NOT NULL,
        cost REAL NOT NULL
    );
    """)

    connection.commit()

def add_item(item_name: str, quantity: int, cost: float):
    try:
        cursor.execute("""
        INSERT INTO inventory (item_name, quantity, cost) 
        VALUES (?, ?, ?)
        """, (item_name, quantity, cost))
        connection.commit()
        print("Item added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding item: {e}")

def view_inventory():
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_item_in_inventory(item_name: str):
    cursor.execute("SELECT * FROM inventory WHERE item_name = ?", (item_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_item(item_id: int):
    cursor.execute("DELETE FROM inventory WHERE item_id = ?", (item_id,))
    connection.commit()
    print(f"Item with ID {item_id} deleted.")