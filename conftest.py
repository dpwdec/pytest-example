import pytest
from database import Session

@pytest.fixture
def create_db():
    return "db"

@pytest.fixture(scope="module")
def db_session():
    session = Session()
    yield session
    session.close()