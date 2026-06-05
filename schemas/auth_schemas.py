from pydantic import BaseModel, Field, EmailStr


class LoginReq(BaseModel):
    __tablename__ = "Auth"

    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    token_type: str
    user_id: str
    email: str

    class Config:
        from_attributes = True