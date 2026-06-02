from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/postgres'

ENGINE = create_engine(DATABASE_URL)

SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()

def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


def create_db():  
    # BASE.metadata.drop_all(bind=ENGINE)
    BASE.metadata.create_all(bind=ENGINE)