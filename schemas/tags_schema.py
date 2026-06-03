from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class TagsRequest(BaseModel):
    name = Field(..., max_length=20)
    color = Optional[str] = Field(None, max_length=7)


class TaskObj(BaseModel):
    id: UUID
    name: str
    color: str

    class Config:
        from_attributes = True


class TagsResponse(BaseModel):
    data: TaskObj
    sattus: int
    message: str

    class Config:
        from_attributes = True
