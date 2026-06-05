from models.user_models import User
from schemas.users_schemas import UserRequest, UserResponse
from fastapi import HTTPException
from models.enums.enums import UserRole
from datetime import datetime
from sqlalchemy.orm import Session
from uuid import uuid4

from utils.helpers import create_hash_password


class UserService:
    @staticmethod
    def create_user(user_request: UserRequest, db: Session) -> UserResponse:
        # Here you would typically hash the password and save the user to the database
        # For demonstration, we will just return a UserResponse object

        existing_user = db.query(User).filter(User.email == user_request.email).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            id=str(uuid4()),
            full_name=user_request.full_name,
            email=user_request.email,
            hashed_password=create_hash_password(user_request.password),
            role=user_request.role,
            is_active=True,
            created_at=datetime.utcnow().isoformat() + "Z",
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()
