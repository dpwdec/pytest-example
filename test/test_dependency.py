from ape import Ape
from banana import Banana

def test_dep(mocker):
    b = Banana("")
    mocker.patch