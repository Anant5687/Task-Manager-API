from sqlalchemy import Column, String
from db.conn import BASE



class TagsModel(BASE):
    __tablename__ = "tags"

    id = Column(String, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    color = Column(String(7), nullable=True, unique=False)
