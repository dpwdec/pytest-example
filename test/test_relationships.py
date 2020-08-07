import pytest
from database import Base, db, Session
from user.model import User, Address

@pytest.fixture(scope="module", autouse=True)
def setup_base():
    Base.metadata.drop_all(bind=db, tables=[User.__table__, Address.__table__])
    Base.metadata.create_all(db)

def test_db_relationships(db_session):
    new_user = User(name="Lomothy", age=25)
    new_user.addresses = [
        Address(email="lomothy@lom-world.net"),
        Address(email="lomothy_lommington@googlemail.co.uk")
    ]

    db_session.add(new_user)
    db_session.commit()

    lomothy = db_session.query(User).filter(User.name == "Lomothy").first()
    assert len(lomothy.addresses) == 2

def test_db_child(db_session):
    result = db_session.query(Address).filter(Address.user_id == 1)
    assert result.count() == 2

