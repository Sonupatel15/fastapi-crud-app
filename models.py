from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    phone_no: str
    address: str
