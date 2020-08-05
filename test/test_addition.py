from mathematic.utils import add

class TestClass():
    def test_answer(self):
        assert add(1) == 2

    def test_wrong(self):
        assert add(2) == 3