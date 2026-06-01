from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, Boolean
from models.enums.enums import UserRole

class User():
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    full_name = Column(String(100), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.MEMBER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    def __init__(self, id, full_name, email, hashed_password, role, is_active, created_at):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.hashed_password = hashed_password
        self.role = role
        self.is_active = is_active
        self.created_at = created_at