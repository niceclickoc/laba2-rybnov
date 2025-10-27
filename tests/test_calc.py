import math
import pytest
from calculator import add, sub, mul, div, pow_

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(-2, -2) == 0

def test_mul():
    assert mul(4, 3) == 12
    assert mul(-2, 4) == -8

def test_div_ok():
    assert div(10, 2) == 5
    assert div(-9, 3) == -3

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)

def test_pow_():
    assert pow_(2, 3) == 8
    assert math.isclose(pow_(9, 0.5), 3.0)
