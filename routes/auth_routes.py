from fastapi import APIRouter, Depends, HTTPException
from schemas.auth_schemas import LoginReq, LoginResponse
from db.conn import get_db
from sqlalchemy.orm import Session
from models.user_models import User
from utils.helpers import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
def login(data: LoginReq, db: Session = Depends(get_db)) -> LoginResponse:
    is_user = db.query(User).filter(User.email == data.email).first()

    if not is_user:
        raise HTTPException(status_code=404, detail=f"User not found with {data.email}")

    is_verify = verify_password(data.password, is_user.hashed_password)

    if not is_verify:
        raise HTTPException(status_code=400, detail="Wrong password entered")
    
    token = create_access_token({
        "email": data.email,
        "password": data.password
    })

    # token = create_access_token(data)

    return {
        "token": token,
        "token_type": "Bearer",
        "user_id": is_user.id,
        "email": data.email,
    }
