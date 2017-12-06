import pytest
from my_app.Numbers_pairs import pairs


def test_smoke():
    assert pairs([1, 9])


def test_type():
    assert type(pairs([1, 9])) == list


@pytest.mark.parametrize("test_input,expected", [
    ([1, 9, 5, 5, 3, 8], (1, 9)),
    ([1, 9, 5, 5, 3, 8], (5, 5)),
])
def test_positive(test_input, expected):
    assert expected in pairs(test_input)


def test_results_uniqueness():
    assert (9, 1) not in pairs([1, 9, 5, 5, 3, 1])


def test_results_uniqueness_2():
    assert pairs([5, 5, 5, 5]).count((5, 5)) == 1


# @pytest.mark.debug
def test_sum():
    assert pairs([1, 9, 4], s=5) == [(1, 4)]


def test_all_pairs():
    assert pairs([1, 9, 1], all_pairs=True) == [(1, 9), (9, 1)]


@pytest.mark.parametrize("test_input,expected,exp_message", [
    ([1], ValueError, "At least 2 numbers required"),
    (1, TypeError, "Only list of digits accepted"),
    ([1, "a"], TypeError, "Only list of digits accepted"),
])
def test_few_numbers(test_input, expected, exp_message):
    with pytest.raises(expected, match=exp_message):
        pairs(test_input)
