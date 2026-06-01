from pydantic import BaseModel, EmailStr
from models.enums.enums import UserRole
from uuid import UUID


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
    created_at: str

    class Config:
        from_attributes = True