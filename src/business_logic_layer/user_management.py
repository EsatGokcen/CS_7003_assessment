from src.data_access_layer.users_table import add_user, view_users, delete_user

# Registers a new user with basic validation.
def register_user(username: str, password: str, email: str, is_admin: bool = False) -> str:
    if not username or not password or not email:
        return "Error: All fields are required."
    if "@" not in email or "." not in email:
        return "Error: Invalid email format."
    add_user(username, password, email, is_admin)
    return "User registered successfully."

# Fetches and returns all users.
def list_users():
    return view_users()

# Deletes a user based on the ID.
def remove_user(user_id: int):
    return delete_user(user_id)