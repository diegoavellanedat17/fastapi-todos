import pytest
from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.services.auth import create_access_token, get_current_user
from app.models.user import User
from app.database.base import Base
from app.services.user_service import get_user_by_email
import os

os.environ["SECRET_KEY"] = "test_secret_key"
os.environ["ALGORITHM"] = "HS256"

@pytest.fixture(scope="module")
def db():
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    yield connection
    connection.close()

def mock_get_current_user(db: Session, token: str):
    payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user = get_user_by_email(db, email=email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

def test_create_access_token():
    # test data
    user_data = {"sub": "testuser@example.com"}
    access_token = create_access_token(user_data)

    # Validate token
    assert isinstance(access_token, str)
