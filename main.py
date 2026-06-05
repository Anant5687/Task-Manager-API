from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.projects_routes import router as project_router
from routes.tasks_routes import router as task_router
from routes.tags_routes import router as tags_router
from routes.file_routes import router as file_router
from routes.auth_routes import router as auth_router
from db.conn import create_db

app = FastAPI()

create_db()


@app.get("/")
def read_root():
    return {"hello"}


@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "OK"}


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(tags_router)
app.include_router(file_router)
