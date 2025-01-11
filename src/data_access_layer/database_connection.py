import sqlite3
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Points to src

# Ensure the database directory exists in the src directory
db_dir = os.path.join(BASE_DIR, "database")
os.makedirs(db_dir, exist_ok=True)

# Path to the database
db_path = os.path.join(db_dir, "brew_and_bite.db")

# SQLite3 Connection (for DAL)
def get_connection():
    return sqlite3.connect(db_path)

# SQLAlchemy Setup (for BLL)
DATABASE_URL = f"sqlite:///{db_path}"  # SQLAlchemy-compatible database URL
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Utility function for SQLAlchemy session management
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

# Debugging the database path
if __name__ == "__main__":
    print(f"Database directory: {db_dir}")
    print(f"Database path: {db_path}")
