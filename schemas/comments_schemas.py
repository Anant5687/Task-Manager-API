from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List


class CommentsRequest(BaseModel):
    tid: str
    content: str = Field(..., max_length=500)


class CommentObj(BaseModel):
    id: str
    tid: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class CommentsResponse(BaseModel):
    data: CommentObj
    status: int
    message: str

    class Config:
        from_attributes = True


class CommentsListResponse(BaseModel):
    data: List[CommentObj]
    status: int
    message: str

    class Config:
        from_attributes = True
