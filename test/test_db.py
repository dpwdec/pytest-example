import pytest
from database import Base, db, Session
from user.model import User

@pytest.fixture(scope="module", autouse=True)
def setup_base():
    Base.metadata.drop_all(bind=db, tables=[User.__table__])
    Base.metadata.create_all(db)
    session = Session()
    change_user = User(name="Mike", age=44)
    session.add(change_user)
    session.commit()
    session.close()

@pytest.fixture(scope="module")
def db_session():
    session = Session()
    return session

def test_add_to_db(db_session):
    new_user = User(name="Dec", age=50)
    db_session.add(new_user)
    db_session.commit()
    assert True

def test_query_db(db_session):
    result = db_session.query(User).filter(User.name == "Dec")
    assert result[0].name == "Dec"

def test_update_db(db_session):
    result = db_session.query(User).filter(User.name == "Mike")
    result[0].age += 2
    db_session.commit()
    result = db_session.query(User).filter(User.age == 46)
    assert result[0].name == "Mike"