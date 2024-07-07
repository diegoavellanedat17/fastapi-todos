from fastapi import FastAPI
from .database import init_db
from .routers import users

app = FastAPI()

init_db()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}