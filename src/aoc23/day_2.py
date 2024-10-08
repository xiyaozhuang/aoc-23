def part_1(data):
    start = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    total = 0

    for string in data:
        name, game = string.split(":")

        subgames = game.split(";")
        hands = [subgame.split(",") for subgame in subgames]

        for hand in hands:
            impossible = False

            for cubes in hand:
                cube = cubes.strip().split(" ")
                n = int(cube[0])
                colour = cube[1]

                if n > start[colour]:
                    impossible = True

            if impossible:
                break

        if not impossible:
            total += int(name.split(" ")[1])

    return total


def part_2(data):
    total = 0

    for string in data:
        name, game = string.split(":")

        subgames = game.split(";")
        hands = [subgame.split(",") for subgame in subgames]

        fewest = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for hand in hands:
            for cubes in hand:
                cube = cubes.strip().split(" ")
                n = int(cube[0])
                colour = cube[1]

                if n > fewest[colour]:
                    fewest[colour] = n

        total += fewest["red"] * fewest["green"] * fewest["blue"]

    return total
