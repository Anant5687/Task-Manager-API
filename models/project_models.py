from sqlalchemy import Column, Integer, String, TIMESTAMP


class Project():
    __tablename__ = 'projects'

    id = Column(String, primary_key=True)
    name = Column(String(100), unique=False, nullable=False)
    description = Column(String(500), nullable=True)
    owner_id = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)