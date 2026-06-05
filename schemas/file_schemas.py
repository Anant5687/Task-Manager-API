from pydantic import BaseModel, Field
from uuid import UUID


class FileRequest(BaseModel):
    filename = str
    task_id = str
    uploaded_by = UUID = Field(..., max_length=500)


class FileResponse(BaseModel):
    id: UUID
    filename: str
    url: str
    task_id: str
    uploaded_by: str

    class Config:
        from_attributes = True
