import sqlite3
import os

# Ensure the database directory exists
db_dir = "database"
os.makedirs(db_dir, exist_ok=True)

# Path to the database
db_path = os.path.join(db_dir, "brew_and_bite.db")

def get_connection():
    return sqlite3.connect(db_path)
