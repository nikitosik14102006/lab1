from mymath.arithmetic import add, divide
import pytest
import mymath

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),

    (0, 0, 0),
    (-5, -5, -10),
    (-10, 5, -5),
    (999999999, 1, 1000000000)
])
def test_add(a, b, expected):
    assert mymath.add(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        mymath.divide(10, 0)

def test_divide_nominal():
    assert mymath.divide(10, 2) == 5.0