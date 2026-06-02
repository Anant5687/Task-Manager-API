from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class ProjectRequest(BaseModel):
    name: str= Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    owner_id: UUID
    

class ProjectData(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    owner_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class ProjectResponse(BaseModel):
    status: int
    data: ProjectData
    message: str
    
    class Config:
        from_attributes = True