from src.data_access_layer.database_connection import Base, engine
from src.business_logic_layer.populate_mock_data import populate_mock_data

# Create all tables in the database and populate with mock data.
def initialize_database():
    try:
        # Drop all existing tables (optional, for a fresh start)
        print("Dropping existing tables...")
        Base.metadata.drop_all(engine)

        # Create new tables
        print("Creating tables...")
        Base.metadata.create_all(engine)
        print("Tables created successfully.")

        # Populate database with mock data
        print("Populating database with mock data...")
        populate_mock_data()
        print("Database populated successfully.")

    except Exception as e:
        print(f"An error occurred during initialization: {e}")

if __name__ == "__main__":
    initialize_database()
