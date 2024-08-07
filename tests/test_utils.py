from aoc23.utils import find_all


def test_findall():
    s = "abab"
    p = "a"

    expected = [0, 2]
    output = list(find_all(p, s))

    assert output == expected
