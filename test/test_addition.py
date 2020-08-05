from mathematic.utils import add
import pytest

@pytest.fixture
def create_message():
    return "Message"

class TestClass():
    def test_answer(self):
        assert add(1) == 2

    def test_wrong(self):
        assert add(2) == 3

    def test_msg(self, create_message):
        assert create_message == "Message"

    def test_db(self, create_db):
        assert create_db == "db"