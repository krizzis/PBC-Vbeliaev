import pytest
from Day3.my_app.Numbers_pairs import pairs


def test_smoke():
    assert pairs([1, 9])


def test_type():
    assert type(pairs([1, 9])) == list


def test_simple_list():
    assert pairs([1, 9]) == [(1, 9)]


def test_several_results_list():
    assert (1, 9) and (5, 5) in pairs([1, 9, 5, 5, 3, 8])


def test_results_uniqueness():
    assert (9, 1) not in pairs([1, 9, 5, 5, 3, 1])


def test_results_uniqueness_2():
    assert pairs([5, 5, 5, 5]).count((5, 5)) == 1


def test_sum():
    assert pairs([1, 9, 4], s=5) == [(1, 4)]


def test_all_pairs():
    assert pairs([1, 9, 1], all_pairs=True) == [(1, 9), (9, 1)]


def test_few_numbers():
    with pytest.raises(ValueError, match="At least 2 numbers required"):
        pairs([1])


def test_string():
    with pytest.raises(TypeError, match="Only digits accepted"):
        pairs([1, "a"])

