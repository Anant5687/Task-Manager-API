from models.user_models import User
from schemas.users_schemas import UserRequest, UserResponse
from fastapi import HTTPException
from models.enums.enums import UserRole
from uuid import uuid4
from datetime import datetime



class UserService:
    @staticmethod
    def create_user(user_request: UserRequest) -> UserResponse:
        # Here you would typically hash the password and save the user to the database
        # For demonstration, we will just return a UserResponse object
        user = User(
            id=uuid4(),
            full_name=user_request.full_name,
            email=user_request.email,
            hashed_password="hashed_" + user_request.password,
            role=user_request.role,
            is_active=True,
            created_at=datetime.utcnow().isoformat() + "Z"
        )
        return UserResponse.from_orm(user)