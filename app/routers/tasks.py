from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import create_task, get_tasks, get_task_by_id, update_task, delete_task
from app.dependencies import get_db
from app.services.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[Task])
def read_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_tasks(db=db, user_id=current_user.id)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = get_task_by_id(db=db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = update_task(db=db, task_id=task_id, task=task, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=Task)
def delete_existing_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = delete_task(db=db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task
