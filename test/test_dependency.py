from ape import Ape
from banana import Banana

def test_dep(mocker):
    b = mocker.Mock()
    b.get_flavor.return_value = "Chocolate"
    a = Ape(b)
    assert a.eat_banana() == "I eat a banana with flavor Chocolate"