from os import listdir

import aoc23


def load_data(path):
    """Reads all the text files from a directory at the given path and returns a dictionary.
    The keys are the names of the files without the extension and the values are the lines of the files.
    """

    data = {}

    for name in listdir(path):
        with open(f"{path}/{name}") as file:
            key = name.split(".")[0]
            data[key] = file.readlines()

    return data


def get_modules(module, pattern, test):
    """Returns all the modules that have the start of their name matching the pattern.
    If test is True, it only returns the aoc23.day_1 module.
    """

    if test:
        return [aoc23.day_1]

    modules = []

    for name in dir(module):
        if name.startswith(pattern):
            modules.append(getattr(module, name))

    return modules


def get_solutions(data, test=False):
    """Returns the solutions of the given data using the aoc23 package.
    If test is True, it only returns the solutions for the first day.
    """

    solutions = {}
    modules = get_modules(aoc23, "day", test)

    for module in modules:
        key = module.__name__.split(".")[1]
        functions = get_modules(module, "part", test=False)

        solutions[key] = (
            functions[0](data[key]),
            functions[1](data[key]),
        )

    return solutions


def find_all(p, s):
    "Yields all the positions of the pattern p in the string s."

    i = s.find(p)

    while i != -1:
        yield i

        i = s.find(p, i + 1)
