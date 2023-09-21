import unittest
from calculating import area


class TestArea(unittest.TestCase):

    def test_calculate_circle(self):
        result = area.calculate_circle(10)
        self.assertEqual(result, 314.159)

    def test_calculate_triangle(self):
        result = area.calculate_triangle(4, 2, 3)
        self.assertEqual(result, 2.905)

    def test_right_triangle(self):
        result = area.right_triangle(2, 3, 3.61)
        self.assertEqual(result, True)

    def test_calculate_unknown(self):
        first_result = area.calculate_unknown('circle', 10)
        self.assertEqual(first_result, 314.159)
        second_result = area.calculate_unknown('triangle', 4, 2, 3)
        self.assertEqual(second_result, 2.905)


if __name__ == "__main__":
    unittest.main()