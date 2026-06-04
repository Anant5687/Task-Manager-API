from db.conn import BASE
from sqlalchemy import Column, String
import uuid


class FileModel(BASE):
    __tablename__ = "file"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    filename = Column(String, nullable=False)
    url = Column(String, nullable=False)
    task_id = Column(String, nullable=False)
    uploaded_by = Column(String, nullable=False)
