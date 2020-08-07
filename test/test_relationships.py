import pytest
from database import Base, db, Session
from user.model import User, Address

@pytest.fixture(scope="module", autouse=True)
def setup_base():
    Base.metadata.drop_all(bind=db, tables=[User.__table__, Address.__table__])
    Base.metadata.create_all(db)

