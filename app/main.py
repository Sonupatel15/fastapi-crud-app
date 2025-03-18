from fastapi import FastAPI, HTTPException, Query, status
from typing import List

from app.models import User, UserCreate, UserUpdate, Message
from app.storage import users_db

# Create FastAPI instance
app = FastAPI(
    title="Users API",
    description="A simple API for managing users",
    version="1.0.0",
)


@app.post("/users/", response_model=Message, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> Message:
    """
    Create a new user with the provided details.
    Returns 400 if a user with the same ID already exists.
    """
    if user.id in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User with this ID already exists"
        )
    
    # Convert UserCreate model to User model and store
    users_db[user.id] = User(
        id=user.id,
        name=user.name,
        phone_no=user.phone_no,
        address=user.address
    )
    
    return Message(message="User created successfully")


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int) -> User:
    """
    Retrieve a user by ID.
    Returns 404 if the user doesn't exist.
    """
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    return user


@app.get("/users/", response_model=List[User])
def list_users() -> List[User]:
    """List all users in the database."""
    return list(users_db.values())


@app.get("/users/search/", response_model=List[User])
def search_users(name: str = Query(None)) -> List[User]:
    """
    Search for users by name.
    Returns an empty list if no users are found.
    """
    if name:
        # Case-insensitive search
        filtered_users = [
            user for user in users_db.values() 
            if name.lower() in user.name.lower()
        ]
        return filtered_users
    
    # Return all users if no name is provided
    return list(users_db.values())


@app.put("/users/{user_id}", response_model=Message)
def update_user(user_id: int, user_update: UserUpdate) -> Message:
    """
    Update user details by ID.
    Only updates the fields that are provided.
    Returns 404 if the user doesn't exist.
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    # Get the existing user
    existing_user = users_db[user_id]
    
    # Update only the fields that are provided
    update_data = user_update.model_dump(exclude_unset=True)
    
    # Create updated user dictionary
    updated_user_dict = existing_user.model_dump()
    updated_user_dict.update(update_data)
    
    # Convert back to User model and update in database
    users_db[user_id] = User(**updated_user_dict)
    
    return Message(message="User updated successfully")


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int) -> Message:
    """
    Delete a user by ID.
    Returns 404 if the user doesn't exist.
    """
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    
    del users_db[user_id]
    
    return Message(message="User deleted successfully")