from db.conn import BASE
from sqlalchemy import Column, String


class FileModels(BASE):
    __tablename__ = "file"

    id = Column(String, primary_key=True)
    filename = Column(String, nullable=False)
    url = Column(String, nullable=False)
    task_id = Column(String, nullable=False)
    uploaded_by = Column(String, nullable=False)
