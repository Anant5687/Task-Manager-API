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
from schemas.comments_schemas import (
    CommentsRequest,
    CommentsResponse,
    CommentsListResponse,
)
from models.comments_models import CommentsModel


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

    @staticmethod
    def add_comment(data: CommentsRequest, db: Session) -> CommentsResponse:
        task = TaskService.check_task(data.tid, db)

        comment = CommentsModel(
            id=uuid4(),
            tid=data.tid,
            content=data.content,
            created_at=datetime.utcnow().isoformat() + "Z",
        )

        db.add(comment)
        db.commit()
        db.refresh(comment)

        return {"status": 201, "message": "Comment added successfully", "data": comment}

    @staticmethod
    def get_comments(task_id: str, db: Session) -> CommentsListResponse:
        task = TaskService.check_task(task_id, db)

        if not task:
            raise HTTPException(status_code=404, detail=f"No task found with {task_id}")

        comments = db.query(CommentsModel).filter(CommentsModel.tid == task_id).all()

        return {
            "status": 200,
            "message": "Comments retrieved successfully",
            "data": comments,
        }

    @staticmethod
    def check_comment(comment_id: str, db: Session):
        comment = db.query(CommentsModel).filter(CommentsModel.id == comment_id).first()

        if not comment:
            raise HTTPException(
                status_code=404, detail=f"No comment found with this {comment_id}"
            )

        return comment

    @staticmethod
    def update_comment(data: CommentsRequest, db: Session) -> CommentsResponse:
        comment = TaskService.check_comment(data.tid, db)

        for key, value in data.dict().keys():
            setattr(comment, key, value)

        db.commit()
        db.refresh(comment)

        return {
            "status": 200,
            "message": "Comment updated successfully",
            "data": comment,
        }

    @staticmethod
    def delete_comment(comment_id: str, db: Session) -> CommentsResponse:
        comment = TaskService.check_comment(comment_id, db)

        db.delete(comment)
        db.commit()

        return {
            "status": 200,
            "message": "Comment deleted successfully",
            "data": comment,
        }
