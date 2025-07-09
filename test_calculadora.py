import pytest
from calculadora import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2
   

def test_multiplica():
    assert multiplica(2, 3) == 6
   

def test_divide():
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0) 