from aoc23.day_2 import part_1, part_2


def test_part_1():
    with open("data/tests/day_2a.txt") as file:
        data = file.readlines()

    expected = 8
    output = part_1(data)

    assert output == expected


def test_part_2():
    with open("data/tests/day_2b.txt") as file:
        data = file.readlines()

    expected = 2286
    output = part_2(data)

    assert output == expected
