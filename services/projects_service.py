from models.project_models import Project
from models.user_models import User
from schemas.projects_schemas import ProjectRequest, ProjectResponse
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from uuid import uuid4


class ProjectService:
    @staticmethod
    def create_project(project_req:ProjectRequest, db: Session) -> ProjectResponse:
        is_user = db.query(User).filter(User.id == str(project_req.owner_id)).first()

        if not is_user:
            raise HTTPException(
                status_code=404,
                detail=f"User not found with {project_req.owner_id}"
            )
        
        project = Project(
            id= str(uuid4()),
            name = project_req.name,
            description = project_req.description,
            owner_id = project_req.owner_id,
            created_at=datetime.utcnow().isoformat() + "Z"
        )

        return {"status": 201, "data": project, "message": "Project created successfully"}