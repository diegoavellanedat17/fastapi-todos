import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.services.user_service import create_user, get_user_by_email, verify_password
from app.schemas.user import UserCreate
from app.database.base import Base
from sqlalchemy.exc import IntegrityError

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def db():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

def test_create_user(db):
    user_data = UserCreate(username="testuser", email="testuser@example.com", password="testpassword")
    user = create_user(db, user_data)
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert verify_password("testpassword", user.hashed_password)

def test_get_user_by_email(db):
    user_data = UserCreate(username="testuser3", email="testuser3@example.com", password="testpassword")
    user = create_user(db, user_data)
    fetched_user = get_user_by_email(db, email="testuser3@example.com")
    assert fetched_user.username == "testuser3"
    assert fetched_user.email == "testuser3@example.com"

def test_create_duplicate_user(db):
    user_data = UserCreate(username="testuser2", email="testuser2@example.com", password="testpassword")
    create_user(db, user_data)
    
    with pytest.raises(IntegrityError):
        duplicate_user_data = UserCreate(username="testuser2", email="testuser2@example.com", password="testpassword")
        create_user(db, duplicate_user_data)
