from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_id(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()

def update_task(db: Session, task_id: int, task: TaskUpdate, user_id: int):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    print(db_task)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
