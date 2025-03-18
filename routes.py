from fastapi import APIRouter, HTTPException
from models import User
from .database import users_db

router = APIRouter()

# Create a new user
@router.post("/users/", status_code=201)
def create_user(user: User):
    # Check if user with the same ID already exists
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")

    users_db.append(user)
    return {"message": "User created successfully"}

# Get user by ID
@router.get("/users/{id}")
def get_user(id: int):
    for user in users_db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
