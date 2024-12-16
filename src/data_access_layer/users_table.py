import sqlite3
from src.data_access_layer.database_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

def create_users_table():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        is_admin BOOLEAN DEFAULT 0
    )
    """)

    connection.commit()

def add_user(username: str, password: str, email: str, is_admin: bool = False):
    try:
        cursor.execute("""
        INSERT INTO Expenses (user_id, date, amount, category, description)
        VALUES (?, ?, ?, ?, ?)
        """, (username, password, email, is_admin))
        connection.commit()
        print("Expense added successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)