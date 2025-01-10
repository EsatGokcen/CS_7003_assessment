from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session
from src.data_access_layer.database_connection import Base, get_db

# SQLAlchemy User Model
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}', is_admin={self.is_admin})>"

# User-related functionality
def register_user(username: str, password: str, email: str, is_admin: bool = False) -> str:
    if not username or not password or not email:
        return "Error: All fields are required."
    if "@" not in email or "." not in email:
        return "Error: Invalid email format."

    session: Session = next(get_db())
    try:
        # Check if username or email already exists
        existing_user = session.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            return "Error: Username or email already exists."

        # Create and add new user
        new_user = User(username=username, password=password, email=email, is_admin=is_admin)
        session.add(new_user)
        session.commit()
        return "User registered successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()

def update_user(user_id: int, username: str = None, password: str = None, email: str = None) -> str:
    session: Session = next(get_db())
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return f"Error: User with ID {user_id} does not exist."

        if username:
            user.username = username
        if password:
            user.password = password  # Ensure passwords are hashed before saving
        if email:
            user.email = email

        session.commit()
        return f"User with ID {user_id} updated successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()

def list_users():
    session: Session = next(get_db())
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        session.close()

def remove_user(user_id: int) -> str:
    session: Session = next(get_db())
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return f"Error: User with ID {user_id} does not exist."

        session.delete(user)
        session.commit()
        return f"User with ID {user_id} deleted successfully."
    except Exception as e:
        session.rollback()
        return f"Error: {str(e)}"
    finally:
        session.close()
