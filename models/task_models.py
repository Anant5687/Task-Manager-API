from sqlalchemy import String, Column, Enum, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from db.conn import BASE
from models.enums.enums import TaskPriority, TaskStatus


class TaskModel(BASE):
    __tablename__ = "tasks"

    id = Column(String, unique=True, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    due_date = Column(TIMESTAMP)
    status = Column(Enum(TaskStatus))
    priority = Column(Enum(TaskPriority))
    project_id = Column(String)
    assign = Column(String, nullable=True)
