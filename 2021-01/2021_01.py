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


def group_measurements(values):
    new_value_list = []
    for i in range(len(values) - 2):
        _sum = values[i] + values[i + 1] + values[i + 2]
        new_value_list.append(_sum)
    return new_value_list


def part_one(filename):
    measurements = read_numbers(filename)
    return count_increases(measurements)


def part_two(filename):
    measurements = read_numbers(filename)
    grouped_measurements = group_measurements(measurements)
    return count_increases(grouped_measurements)


class PartOne(unittest.TestCase):
    def test_example(self):
        self.assertEqual(7, part_one("2021_01_example.txt"))

    def test_puzzle(self):
        self.assertEqual(1475, part_one("2021_01_puzzle.txt"))


class PartTwo(unittest.TestCase):
    def test_example(self):
        self.assertEqual(5, part_two("2021_01_example.txt"))

    def test_puzzle(self):
        self.assertEqual(1516, part_two("2021_01_puzzle.txt"))


if __name__ == '__main__':
    unittest.main()
