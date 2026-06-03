from fastapi import APIRouter, Depends
from schemas.tags_schema import TagsRequest, TagsResponse
from sqlalchemy.orm import Session
from db.conn import get_db
from services.tags_service import TagsService

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("/{tag_id}", response_model=TagsResponse)
def get_tag(tag_id: str, db: Session = Depends(get_db)):
    return TagsService.get_task(tag_id, db)


@router.post("/", response_model=TagsResponse)
def create_tag(data: TagsRequest, db: Session = Depends(get_db)):
    return TagsService.create_tag(data, db)
