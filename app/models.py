from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Base model with common user attributes"""
    name: str
    phone_no: str
    address: str


class User(UserBase):
    """Complete user model with ID"""
    id: int


class UserCreate(UserBase):
    """Model for user creation"""
    id: int


class UserUpdate(BaseModel):
    """Model for user updates that makes all fields optional"""
    name: str | None = None
    phone_no: str | None = None
    address: str | None = None


class Message(BaseModel):
    """Standard message response model"""
    message: str