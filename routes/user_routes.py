from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users" , tags=["Users"])

from services.users_service import UserService
from schemas.users_schemas import UserRequest, UserResponse

@router.post("/", response_model=UserResponse)
def create_user(user_request: UserRequest):
    return UserService.create_user(user_request)