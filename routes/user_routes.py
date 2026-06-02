from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users" , tags=["Users"])

from services.users_service import UserService
from schemas.users_schemas import UserRequest, UserResponse
from sqlalchemy.orm import Session
from db.conn import get_db

@router.post("/", response_model=UserResponse)
def create_user(user_request: UserRequest, db: Session = Depends(get_db)):
    return UserService.create_user(user_request, db)

@router.get("/get-all/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)