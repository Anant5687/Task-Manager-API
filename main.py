from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.projects_routes import router as project_router
from db.conn import create_db


app = FastAPI()
app.include_router(user_router)
app.include_router(project_router)

create_db()

@app.get("/")
def read_root():
    return {"hello"}

@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "OK"}