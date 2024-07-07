from fastapi import FastAPI
from .database.init_db import init_db
from .routers import users, tasks

app = FastAPI()

init_db()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


@app.get("/health")
def health_check():
    return {"status": "healthy"}