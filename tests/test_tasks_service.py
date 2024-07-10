import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.database.base import Base
from app.services.task_service import create_task, get_tasks, get_task_by_id, update_task, delete_task

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_get_tasks(db):
    user_id = 1  
    task_data_1 = TaskCreate(title="Task 1", description="Task 1 description")
    task_data_2 = TaskCreate(title="Task 2", description="Task 2 description")
    create_task(db, task_data_1, user_id)
    create_task(db, task_data_2, user_id)


    tasks = get_tasks(db, user_id)

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_create_task(db):
    user_id = 1  
    task_data = TaskCreate(title="Test Task", description="Testing task creation")

    created_task = create_task(db, task_data, user_id)

    assert created_task.id is not None
    assert created_task.title == "Test Task"
    assert created_task.description == "Testing task creation"
    assert created_task.user_id == user_id



def test_get_task_by_id(db):
    # Test data
    user_id = 1 
    task_data = TaskCreate(title="Test Task", description="Testing get task by id")
    created_task = create_task(db, task_data, user_id)

    fetched_task = get_task_by_id(db, created_task.id, user_id)

    assert fetched_task is not None
    assert fetched_task.title == "Test Task"
    assert fetched_task.description == "Testing get task by id"


def test_update_task(db):
    user_id = 1 
    task_data = TaskCreate(title="Initial Task", description="Initial description")
    created_task = create_task(db, task_data, user_id)

    updated_data = TaskUpdate(title="Updated Task", description="Updated description")

    updated_task = update_task(db, created_task.id, updated_data, user_id)

    assert updated_task is not None
    assert updated_task.id == created_task.id
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated description"

def test_delete_task(db):
    user_id = 1  
    task_data = TaskCreate(title="Task to delete", description="Task to delete description")
    created_task = create_task(db, task_data, user_id)

    deleted_task = delete_task(db, created_task.id, user_id)

    assert deleted_task is not None
    assert deleted_task.id == created_task.id

    fetched_task = get_task_by_id(db, created_task.id, user_id)
    assert fetched_task is None  