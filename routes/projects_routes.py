from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.conn import get_db
from schemas.projects_schemas import (
    ProjectRequest,
    ProjectResponse,
    ProjectsResponse,
    UpdateProject,
)
from services.projects_service import ProjectService

from schemas.tasks_schemas import AllTaskResponse, TaskResponse, TaskCreateRequest

router = APIRouter(prefix="/project", tags=["Projects"])


@router.get("/", response_model=ProjectsResponse)
def get_all_projects(owner_id: str, db: Session = Depends(get_db)):
    return ProjectService.get_all_projects(owner_id, db)


@router.post("/", response_model=ProjectResponse)
def create_project(data: ProjectRequest, db: Session = Depends(get_db)):
    return ProjectService.create_project(data, db)


@router.get("/{id}", response_model=ProjectResponse)
def get_project(id: str, db: Session = Depends(get_db)):
    return ProjectService.get_project(id, db)


@router.put("/{id}", response_model=ProjectResponse)
def replace_project(id: str, data: UpdateProject, db: Session = Depends(get_db)):
    return ProjectService.replace_project(id, data, db)


@router.patch("/{id}", response_model=ProjectResponse)
def update_project(id: str, data: UpdateProject, db: Session = Depends(get_db)):
    return ProjectService.update_project(id, data, db)


@router.delete("/{id}", response_model=ProjectResponse)
def delete_project(id: str, user_id: str, db: Session = Depends(get_db)):
    return ProjectService.delete_project(id, user_id, db)


@router.get("/{p_id}/tasks", response_model=AllTaskResponse)
def get_all_task_in_project(p_id: str, db: Session = Depends(get_db)):
    return ProjectService.get_task_in_project(p_id, db)


@router.post("/{p_id}/tasks", response_model=TaskResponse)
def create_task(
    p_id: str, data: TaskCreateRequest, db: Session = Depends(get_db)
):
    return ProjectService.create_task(p_id, data, db)
