from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"hello"}

@app.get("/health-check")
def health_check():
    return {"status": 200, "message": "OK"}