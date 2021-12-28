import unittest


def count_increases(filename):
    with open(filename, "r") as file:
        previous_value = int(file.readline())
        count_of_increases = 0

        for value in file.readlines():
            current_value = int(value)
            if current_value > previous_value:
                count_of_increases += 1
            previous_value = current_value

        return count_of_increases


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count_increases("example-1.txt"), 7)
        self.assertEqual(count_increases("puzzle-1.txt"), 1475)


if __name__ == '__main__':
    unittest.main()

