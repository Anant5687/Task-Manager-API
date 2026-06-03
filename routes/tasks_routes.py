from fastapi import APIRouter, Depends
from db.conn import get_db
from services.task_service import TaskService
from sqlalchemy.orm import Session
from schemas.tasks_schemas import (
    TaskResponse,
    DeleteTaskReq,
    StatusUpdate,
    TaskAssignReq,
)
from schemas.comments_schemas import CommentsRequest, CommentsResponse, CommentsListResponse

router = APIRouter(prefix="/task", tags=["Tasks"])


@router.get("/{id}", response_model=TaskResponse)
def get_task_by_id(id: str, db: Session = Depends(get_db)):
    return TaskService.get_task_by_id(id, db)


@router.delete("/{id}", response_model=TaskResponse)
def delete_task_by_id(id: str, data: DeleteTaskReq, db: Session = Depends(get_db)):
    return TaskService.delete_task_by_id(id, data, db)


@router.post("/{id}/status", response_model=TaskResponse)
def update_task_status(id: str, data: StatusUpdate, db: Session = Depends(get_db)):
    return TaskService.update_task_status(id, data, db)


@router.post("/{id}/assign", response_model=TaskResponse)
def assign_task(id: str, data: TaskAssignReq, db: Session = Depends(get_db)):
    return TaskService.assign_task(id, data, db)


@router.post("/{id}/comments", response_model=CommentsResponse)
def add_comment(id: str, data: CommentsRequest, db: Session = Depends(get_db)):
    data.tid = id
    return TaskService.add_comment(data, db)


@router.get("/{id}/comments", response_model=CommentsListResponse)
def get_comments(id: str, db: Session = Depends(get_db)):
    return TaskService.get_comments(id, db)
