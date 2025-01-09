import sqlite3
from src.data_access_layer.database_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

def create_sales_items_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_items (
        sales_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (sale_id) REFERENCES sales(sale_id) ON DELETE CASCADE,
        FOREIGN KEY (item_id) REFERENCES inventory(item_id) ON DELETE CASCADE
    );
    ''')

    connection.commit()

def add_sale_item(sale_id: int, item_id: int, quantity: int, price: float):
    try:
        cursor.execute("""
        INSERT INTO sales_items (sale_id, item_id, quantity, price)
        VALUES (?, ?, ?, ?)
        """, (sale_id, item_id, quantity, price))
        connection.commit()
        print("Sale-Item added successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)

def view_sales_items():
    cursor.execute("SELECT * FROM sales_items")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_sales_items_by_sale_id(sale_id: int):
    cursor.execute("SELECT * FROM sales_items WHERE sale_id = ?", (sale_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_sales_items_by_item_id(item_id: int):
    cursor.execute("SELECT * FROM sales_items WHERE item_id = ?", (item_id,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_sales_item(sales_item_id: int):
    cursor.execute("DELETE FROM sales_items WHERE sales_item_id = ?", (sales_item_id,))
    connection.commit()
    print(f"Sales-item with ID {sales_item_id} deleted.")

connection.close()