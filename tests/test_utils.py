import pytest

from aoc23.utils import find_all, get_modules, get_solutions, load_data


def test_load_data():
    expected = {"hello": ["world"]}
    output = load_data("data/dummy")

    assert expected == output


def test_get_modules():
    expected = [pytest.fixture]
    output = get_modules(pytest, "fixture", test=False)

    assert output == expected


def test_get_solutions():
    expected = {"day_1": (55108, 56324)}
    output = get_solutions(load_data("data/problems"), test=True)

    assert output == expected


def test_findall():
    s = "abab"
    p = "a"

    expected = [0, 2]
    output = list(find_all(p, s))

    assert output == expected
