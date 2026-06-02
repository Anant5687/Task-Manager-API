from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.conn import get_db
from schemas.projects_schemas import ProjectRequest, ProjectResponse
from services.projects_service import ProjectService

router = APIRouter(prefix="/project", tags=["Projects"])

@router.post("/", response_model= ProjectResponse)
def create_project(data:ProjectRequest, db: Session = Depends(get_db)):
    return ProjectService.create_project(data, db)