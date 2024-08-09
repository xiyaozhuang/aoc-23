from aoc23.day_1 import part_1, part_2


def test_part_1():
    with open("data/tests/day_1a.txt") as file:
        data = file.readlines()

    expected = 142
    output = part_1(data)

    assert output == expected


def test_part_2():
    with open("data/tests/day_1b.txt") as file:
        data = file.readlines()

    expected = 281
    output = part_2(data)

    assert output == expected
