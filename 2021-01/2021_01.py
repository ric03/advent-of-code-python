import unittest


def read_numbers(filename):
    with open(filename, "r") as file:
        return [int(value) for value in file.readlines()]


def count_increases(measurements):
    count_of_increases = 0

    previous_value = measurements[0]

    for value in measurements:
        if value > previous_value:
            count_of_increases += 1
        previous_value = value

    return count_of_increases


def part_one(filename):
    measurements = read_numbers(filename)
    return count_increases(measurements)


def part_two(filename):
    measurements = read_numbers(filename)
    return count_increases(measurements)


class PartOne(unittest.TestCase):
    def test_example(self):
        self.assertEqual(part_one("2021_01_example.txt"), 7)

    def test_puzzle(self):
        self.assertEqual(part_one("2021_01_puzzle.txt"), 1475)


class PartTwo(unittest.TestCase):
    def test_example(self):
        self.assertEqual(part_two("2021_01_example.txt"), 5)

    def test_puzzle(self):
        self.assertEqual(part_two("2021_01_puzzle.txt"), -1)


if __name__ == '__main__':
    unittest.main()

