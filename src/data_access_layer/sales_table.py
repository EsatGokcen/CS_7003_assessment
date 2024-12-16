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
        VALUES (?, ?, ?)
        """, (date, total_amount, user_id))
        connection.commit()
        print("Sale added successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)

def view_sales():
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_sales_by_date(date: str):
    cursor.execute("SELECT * FROM sales WHERE date = ?", (date,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_sale(sale_id: int):
    cursor.execute("DELETE FROM sales WHERE sale_id = ?", (sale_id,))
    connection.commit()
    print(f"Sale with ID {sale_id} deleted.")

connection.close()