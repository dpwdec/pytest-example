import pytest

class Cobject():
    def __init__(self):
        self.c = 0

@pytest.fixture(scope="module")
def counter():
    cob = Cobject()
    return cob

def test_count_one(counter):
    counter.c += 1
    assert counter.c == 1

def test_count_two(counter):
    assert counter.c == 1