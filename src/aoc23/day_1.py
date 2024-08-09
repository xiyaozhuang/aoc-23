from aoc23.utils import find_all


def part_1(data):
    total = 0

    for string in data:
        digits = []

        for char in string:
            if char.isdigit():
                digits.append(char)

        total += int(digits[0] + digits[-1])

    return total


def part_2(data):
    num_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total = 0

    for string in data:
        nums_pos = {}

        for key, value in num_map.items():
            for pos in find_all(key, string):
                nums_pos[pos] = num_map[key]

            for pos in find_all(value, string):
                nums_pos[pos] = value

        num_first = nums_pos[min(nums_pos.keys())]
        num_last = nums_pos[max(nums_pos.keys())]

        total += int(num_first + num_last)

    return total
