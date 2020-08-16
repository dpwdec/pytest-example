from ape import Ape
from banana import Banana

def test_dep(mocker):
    b = mocker.Mock()
    b.get_flavor.return_value = "Chocolate"
    a = Ape(b)
    assert a.eat_banana() == "I eat a banana with flavor Chocolate"

def test_called(mocker):
    b = mocker.Mock()
    # b.get_flavor.return_value = ""
    a = Ape(b)
    a.eat_banana()
    b.get_flavor.assert_called_with()

def test_called_dep(mocker):
    pass