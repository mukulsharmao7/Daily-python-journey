import pytest

from math_utils import safe_divide


def test_normal():
    assert safe_divide(10, 2) == 5.0


def test_decimal():
    assert safe_divide(7, 2) == 3.5


def test_zero_raises():
    with pytest.raises(ValueError):
        safe_divide(10, 0)


def test_string_raises():
    with pytest.raises(TypeError):
        safe_divide("10", 2)
        
import pytest

from math_utils import safe_divide


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (7, 2, 3.5),
    (0, 5, 0.0),
    (-9, 3, -3.0),
])
def test_divide(a, b, expected):
    assert safe_divide(a, b) == expected


def test_zero_raises():
    with pytest.raises(ValueError):
        safe_divide(10, 0)


def test_string_raises():
    with pytest.raises(TypeError):
        safe_divide("10", 2)