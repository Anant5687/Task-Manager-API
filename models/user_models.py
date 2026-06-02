from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID
from models.enums.enums import UserRole
from db.conn import BASE
from uuid import uuid4

class User(BASE):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    full_name = Column(String(100), unique=False, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.MEMBER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
