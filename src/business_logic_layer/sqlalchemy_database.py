from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLite database path
DATABASE_URL = "sqlite:///../database/brew_and_bite.db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create Declarative Base
Base = declarative_base()

# Create Session Maker
SessionLocal = sessionmaker(bind=engine)

# Utility function for session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
