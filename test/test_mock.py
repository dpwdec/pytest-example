from app import get_operating_system
from app import get_resolution
#from pytest-mock import mocker

def test_get_operating_system(mocker):
    mocker.patch("app.is_windows", return_value=True)
    assert get_operating_system() == 'Windows'

def test_get_operating_linux(mocker):
    mocker.patch("app.is_windows", return_value=False)
    assert get_operating_system() == 'Linux'

def test_high_def(mocker):
    mocker.patch("app.is_4k", return_value=True)
    assert get_resolution() == '4k'