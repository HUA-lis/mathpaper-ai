import unittest

from src.math_tools import average, maximum


class TestMathTools(unittest.TestCase):
    def test_average_with_normal_numbers(self):
        result = average([1, 2, 3])
        self.assertEqual(result, 2)

    def test_average_with_empty_list(self):
        with self.assertRaises(ValueError):
            average([])

    def test_maximum_with_normal_numbers(self):
        result = maximum([1, 5, 3])
        self.assertEqual(result, 5)

    def test_maximum_with_empty_list(self):
        with self.assertRaises(ValueError):
            maximum([])


if __name__ == "__main__":
    unittest.main()
