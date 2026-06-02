from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from models.enums.enums import TaskPriority, TaskStatus

class TaskCreateRequest(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(..., max_length=(500))
    due_date: datetime
    status: TaskStatus
    priority: TaskPriority

class TaskObject(BaseModel):
    id: str
    title : str
    description : str
    due_date : datetime
    status : TaskStatus
    priority : TaskPriority
    project_id : UUID

    class Config:
        from_attributes = True

class TaskResponse(BaseModel):
    status: int
    message: str
    data: TaskObject

    class Config:
        from_attributes = True

class AllTaskResponse(BaseModel):
    status: int
    message: str
    data: list[TaskObject]

    class Config:
        from_attributes = True