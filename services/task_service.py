from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from uuid import uuid4
from models.task_models import TaskModel
from models.user_models import User
from schemas.tasks_schemas import (
    TaskResponse,
    DeleteTaskReq,
    StatusUpdate,
    TaskAssignReq,
)


class TaskService:

    @staticmethod
    def check_task(id: str, db: Session):
        task = db.query(TaskModel).filter(TaskModel.id == id).first()
        return task

    @staticmethod
    def get_task_by_id(id: str, db: Session) -> TaskResponse:
        task = TaskService.check_task(id, db)

        if not task:
            raise HTTPException(status_code=404, detail=f"No task found with {id}")

        return {"status": 200, "message": "Task successfully", "data": task}

    @staticmethod
    def delete_task_by_id(id: str, data: DeleteTaskReq, db: Session) -> TaskResponse:
        existing_user = db.query(User).filter(data.user_id == User.id).first()

        if not existing_user:
            raise HTTPException(
                status_code=404, detail=f"No user found with {data.user_id}"
            )

        task = TaskService.check_task(id, db)

        db.delete(task)
        db.commit()
        return {"status": 200, "message": "Task deleted successfully", "data": task}

    @staticmethod
    def update_task_status(id: str, data: StatusUpdate, db: Session) -> TaskResponse:
        task = TaskService.check_task(id, db)

        task.status = data.status

        db.commit()
        db.refresh(task)

        return {
            "status": 200,
            "message": "Task status changed successfully",
            "data": task,
        }

    @staticmethod
    def assign_task(id: str, data: TaskAssignReq, db: Session) -> TaskResponse:
        task = TaskService.check_task(id, db)

        task.assign = data.assign

        db.commit()
        db.refresh(task)

        return {
            "status": 200,
            "message": "Task assigned successfully",
            "data": task,
        }
