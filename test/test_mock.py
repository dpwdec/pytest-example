from app import get_operating_system
#from pytest-mock import mocker

def test_get_operating_system(mocker):
    mocker.patch("app.is_windows", return_value=True)
    assert get_operating_system() == 'Windows'