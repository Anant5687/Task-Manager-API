from models.project_models import Project
from models.user_models import User
from schemas.projects_schemas import (
    ProjectRequest,
    ProjectResponse,
    ProjectsResponse,
    UpdateProject,
)
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from uuid import uuid4

from schemas.tasks_schemas import TaskCreateRequest, TaskResponse, AllTaskResponse
from models.task_models import TaskModel


class ProjectService:
    @staticmethod
    def create_project(project_req: ProjectRequest, db: Session) -> ProjectResponse:
        is_user = db.query(User).filter(User.id == str(project_req.owner_id)).first()

        if not is_user:
            raise HTTPException(
                status_code=404, detail=f"User not found with {project_req.owner_id}"
            )

        project = Project(
            id=str(uuid4()),
            name=project_req.name,
            description=project_req.description,
            owner_id=project_req.owner_id,
            created_at=datetime.utcnow().isoformat() + "Z",
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return {
            "status": 201,
            "data": project,
            "message": "Project created successfully",
        }

    @staticmethod
    def get_all_projects(owner_id: str, db: Session) -> ProjectsResponse:

        existing_user = db.query(User.id == owner_id).first()

        if not existing_user:
            raise HTTPException(
                status_code=404, detail=f"No user found with {owner_id}"
            )

        print(owner_id, db.query(Project).all())

        projects = db.query(Project).filter(Project.owner_id == str(owner_id)).all()
        return {
            "status": 200,
            "message": "Projects data successfully",
            "data": projects,
        }

    @staticmethod
    def get_project(id: str, db: Session):
        project = db.query(Project).filter(Project.id == id).first()

        if not project:
            raise HTTPException(status_code=400, detail=f"No project found with {id}")

        return {
            "status": 200,
            "message": "Project returned successfully",
            "data": project,
        }

    @staticmethod
    def replace_project(id: str, data: UpdateProject, db: Session):
        project = ProjectService.get_project(id, db)
        for key, value in data.dict().items():
            setattr(project, key, value)

        db.commit()
        db.refresh(project)
        return {
            "status": 200,
            "message": "Project updated successfully",
            "data": project,
        }

    @staticmethod
    def update_project(id: str, data: UpdateProject, db: Session):
        project = ProjectService.get_project(id, db)

        for key, value in data.dict().items():
            setattr(project, key, value)

        db.commit()
        db.refresh(project)
        return {
            "status": 200,
            "message": "Project updated successfully",
            "data": project,
        }

    @staticmethod
    def delete_project(id: str, user_id: str, db: Session):
        project = ProjectService.get_project(id, db)

        user = db.query(User).filter(User.id == user_id).first()

        if user.role != "admin":
            raise HTTPException(
                status_code=400, detail="You are not authorized to delete the task"
            )
        print({project})
        db.delete(project)
        db.commit()
        return {
            "status": 200,
            "message": "Project deleted succesfully",
            "data": project,
        }

    @staticmethod
    def get_task_in_project(pid: str, db: Session) -> AllTaskResponse:
        project = ProjectService.get_project(pid, db)

        tasks = db.query(TaskModel).filter(TaskModel.project_id == pid).all()

        return {"status": 200, "message": "Tasks with the project", "data": tasks}

    @staticmethod
    def create_task(pid: str, data: TaskCreateRequest, db: Session) -> TaskResponse:
        project = ProjectService.get_project(pid, db)

        task = TaskModel(
            id=str(uuid4()),
            title=data.title,
            description=data.description,
            due_date=data.due_date,
            status=data.status,
            priority=data.priority,
            project_id=pid,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return {
            "status": 201,
            "data": task,
            "message": "Task created successfully",
        }
