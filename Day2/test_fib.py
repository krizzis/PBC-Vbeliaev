import pytest
from Fibonacci import fib


def test_smoke():
    assert fib(1)


def test_type():
    assert type(fib(1)) == list


def test_value_1():
    assert fib(1) == [0]


def test_value_2():
    assert fib(2) == [0, 1]


def test_value_3():
    assert fib(7) == [0, 1, 1, 2, 3, 5, 8]


def test_neg_zero():
    with pytest.raises(SystemExit):
        fib(0)


def test_neg_negative_number():
    with pytest.raises(SystemExit):
        fib(-3)


def test_neg_str():
    with pytest.raises(TypeError):
        fib("a")


def test_neg_float():
    with pytest.raises(TypeError):
        fib(1.0)


def test_neg_several_args():
    with pytest.raises(TypeError):
        fib(1, 1)
