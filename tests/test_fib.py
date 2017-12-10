import pytest
from my_app.fibonacci import fib


@pytest.mark.smoke
@pytest.mark.positive
def test_smoke():
    assert fib(1)


@pytest.mark.smoke
@pytest.mark.positive
def test_type():
    assert type(fib(1)) == list


@pytest.mark.positive
@pytest.mark.parametrize("test_input,expected", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
])
def test_positive(test_input, expected):
    assert fib(test_input) == expected


@pytest.mark.negative
@pytest.mark.parametrize("test_input,expected,message", [
    (0, ValueError, "Number must be a positive"),
    (-3, ValueError, "Number must be a positive"),
    (1.0, TypeError, ".*"),
    ((1, 1), TypeError, ".*"),
])
def test_neg_str(test_input, expected, message):
    with pytest.raises(expected, match=message):
        fib(test_input)
