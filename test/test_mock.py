from app import get_operating_system
from app import get_resolution
#from pytest-mock import mocker

def test_get_operating_system(mocker):
    mocker.patch("app.is_windows", return_value=True)
    assert get_operating_system() == 'Windows'

def test_get_operating_linux(mocker):
    mocker.patch("app.is_windows", return_value=False)
    assert get_operating_system() == 'Linux'

def _high_def(mocker):
    mocker.patch("app.is_4k", return_value=True)
    assert get_resolution() == '4k'


"""
Its not clear what advantage of the object mock is, can you mock method return values with this
it seems pretty verbose to have to define a new function for mocking, could I not just set a return value
or do I do that by patching the mocked object, importing into the tests, patching it and then passing it in
but then am I even mocking because the object is coming with all its other stuff?
"""