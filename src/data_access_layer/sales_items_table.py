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
        FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
        FOREIGN KEY (item_id) REFERENCES inventory(item_id)
    );
    ''')

    connection.commit()

connection.close()