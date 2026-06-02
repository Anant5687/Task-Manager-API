from fastapi import FastAPI
from routes.user_routes import router as user_router
from db.conn import create_db


app = FastAPI()
app.include_router(user_router)

create_db()

@app.get("/")
def read_root():
    return {"hello"}

@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "OK"}