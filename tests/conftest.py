import pytest
from typing import Generator
from fastapi.testclient import TestClient
from src.api.main import app
from src.database.session import SessionLocal, engine
from src.database.base import Base

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Create a clean database schema for the test session."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    """Provides a transactional database session for a single test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client() -> Generator:
    """Provides a TestClient for FastAPI endpoints."""
    with TestClient(app) as c:
        yield c