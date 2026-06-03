from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from db.conn import BASE


class CommentsModel(BASE):
    __tablename__ = "comments"
    id = Column(String, primary_key=True)
    tid = Column(String, ForeignKey("tasks.id"), nullable=False)
    content = Column(String(500), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
