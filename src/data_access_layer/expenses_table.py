from src.data_access_layer.database_connection import get_connection
import sqlite3

connection = get_connection()
cursor = connection.cursor()

def create_expenses_table():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)

    connection.commit()

def add_expense(user_id: int, date: str, amount: float, category: str, description: str =None):
    try:
        cursor.execute("""
        INSERT INTO Expenses (user_id, date, amount, category, description)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, date, amount, category, description))
        connection.commit()
        print("Expense added successfully!")
    except sqlite3.Error as e:
        print("An error occurred:", e)

def view_expenses():
    cursor.execute("SELECT * FROM Expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_expenses_by_category(category: str):
    cursor.execute("SELECT * FROM Expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_expense(expense_id: int):
    cursor.execute("DELETE FROM Expenses WHERE expense_id = ?", (expense_id,))
    connection.commit()
    print(f"Expense with ID {expense_id} deleted.")

connection.close()