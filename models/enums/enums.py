from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
    VIEWER = "viewer"

class TaskPriority(str, Enum):
    MEDIUM = "medium"
    LOW = "low"
    HIGH = "high"

class TaskStatus(str, Enum):
    PENDING= "pending"
    REJECTED= "rejected"
    completed="completed"