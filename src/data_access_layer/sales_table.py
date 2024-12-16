import sqlite3
from src.data_access_layer.database_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

def create_sales_table():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        total_amount REAL NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    connection.commit()

def add_sale(date: str, total_amount: float, user_id: int):
    try:
        cursor.execute("""
        INSERT INTO sales (date, total_amount, user_id)
        VALUES (?, ?, ?, ?, ?)
        """, (date, total_amount, user_id))
        connection.commit()
        print("Sale added successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)