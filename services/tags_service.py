from models.tags_models import TagsModel
from schemas.tags_schema import TagsRequest, TagsResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4


class TagsService:
    @staticmethod
    def create_tag(data: TagsRequest, db: Session) -> TagsResponse:
        tag = db.query(TagsModel).filter(TagsModel.name == data.name).first()

        if tag:
            raise HTTPException(status_code=400, detail="Tag already present")

        new_tag = TagsModel(id=uuid4(), name=data.name, color=data.color)

        db.add(new_tag)
        db.commit()
        db.refresh()
        return {"status": 201, "message": "Tag created suiccessfully", "data": new_tag}

    @staticmethod
    def get_task(tag_id: str, db: Session) -> TagsResponse:
        tag = db.query(TagsModel).filter(TagsModel.id == tag_id).first()

        if not tag:
            raise HTTPException(status_code=404, detail=f"No tag found with {tag_id}")

        return {"data": tag, "message": "Tag returned successfully", "status": 200}
