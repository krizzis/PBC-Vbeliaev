import pytest
from Day3.my_app.Fibonacci import fib


def test_smoke():
    assert fib(1)


def test_type():
    assert type(fib(1)) == list


@pytest.mark.parametrize("test_input,expected", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
])
def test_positive(test_input, expected):
    assert fib(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (0,  SystemExit),
    (-3, SystemExit),
    (1.0, TypeError),
    ((1, 1), TypeError),
])
def test_neg_str(test_input, expected):
    with pytest.raises(expected):
        fib(test_input)
