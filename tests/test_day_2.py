from aoc23.day_2 import part_1


def test_part_1():
    with open("data/tests/day_2a.txt") as file:
        data = file.readlines()

    expected = 8
    output = part_1(data)

    assert output == expected
