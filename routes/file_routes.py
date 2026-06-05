from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
import uuid
from models.file_models import FileModel
from db.conn import get_db

router = APIRouter(prefix='/file', tags=["File"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    task_id: str = Form(...),
    uploaded_by: str = Form(...),
    db: Session = Depends(get_db)
):

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Generate URL
    file_url = f"http://localhost:8000/files/{unique_filename}"

    # Save to DB
    db_file = FileModel(
        filename=file.filename,
        url=file_url,
        task_id=task_id,
        uploaded_by=uploaded_by
    )

    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {
        "message": "File uploaded successfully",
        "data": db_file
    }

@router.get("/download/{file_id}")
def download_file(
    file_id: str,
    db: Session = Depends(get_db)
):

    file = db.query(FileModel).filter(
        FileModel.id == file_id
    ).first()

    if not file:
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    file_name = file.url.split("/")[-1]

    path = f"uploads/{file_name}"

    return FileResponse(
        path=path,
        filename=file.filename,
        media_type="application/octet-stream"
    )