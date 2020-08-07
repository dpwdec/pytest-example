import pytest
from database import Base, db, Session
from user.model import User, Address

@pytest.fixture(scope="module", autouse=True)
def setup_base():
    Base.metadata.drop_all(bind=db, tables=[User.__table__, Address.__table__])
    Base.metadata.create_all(db)
    session = Session()
    change_user = User(name="Mike", age=44)
    session.add(change_user)
    session.commit()
    session.close()

def test_add_to_db(db_session):
    new_user = User(name="Dec", age=55)
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

def test_update_attr(db_session):
    mike = db_session.query(User).filter(User.name == "Mike").first()
    setattr(mike, 'age', mike.age + 2)
    db_session.commit()
    mike = db_session.query(User).filter(User.age == 48).first()
    assert mike.name == "Mike"

def test_update_inplace(db_session):
    db_session.query(User).filter(User.name == "Mike").update({'age': (User.age + 2)})
    db_session.commit()
    mike = db_session.query(User).filter(User.age == 50).first()
    assert mike.name == "Mike"

def test_add_multiple(db_session):
    db_session.add_all([
        User(name="John", age=90),
        User(name="Philo", age=98),
        User(name="Paris", age=95)
    ])
    db_session.commit()
    result = db_session.query(User).filter(User.age >= 90)
    assert result.count() == 3