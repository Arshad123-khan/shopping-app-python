'''
Handles user authentication for users and admins, and session management for the shopping app.
'''

import uuid #used to generate unique session IDs
from shopping_app.data import data # Importing the in-memory database

# Function to authenticate user credentials
def authenticate_user(username, password, role):
    if role == 'user':
        account_db = data.users_db
    elif role == 'admin':
        account_db = data.admins_db
    else:
        print("Invalid role specified.")
        return None
    
    # Checking is username exists and password matches
    if username in account_db and account_db[username]['password'] == password:
        # Generate a unique session ID
        session_id = str(uuid.uuid4())
        print(f"{role.capitalize()} '{username}'Authentication successful. Session ID: {session_id}")
        return session_id
    else:
        print("Authentication failed. Invalid username or password.")
        return None
    
# Role check function
def check_role(session_id, role):
    """
    Checks if the given session belongs to a specific role.
    For now, role checking is simulated (would be DB lookup in real app).
    """
    # In a real app, we’d store role in the session table.
    # Here, we'll just simulate it by printing (this will evolve later)
    print(f"Checking if session {session_id} has role '{role}'")
    return True  # Temporary until session storage is implemented