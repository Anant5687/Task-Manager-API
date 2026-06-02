from pydantic import BaseModel, EmailStr
from models.enums.enums import UserRole
from uuid import UUID
from datetime import datetime



class UserRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole


class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True