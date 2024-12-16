from src.data_access_layer.database_connection import get_connection

def create_expenses_table():
    connection = get_connection()
    cursor = connection.cursor()

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