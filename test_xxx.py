import unittest
from xxx import add  # 假设你的函数在一个名为xxx.py的文件里

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.5, 2.5), 1.0)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_large_negative_numbers(self):
        self.assertEqual(add(-1000000, -2000000), -3000000)

    def test_add_large_mixed_numbers(self):
        self.assertEqual(add(1000000, -2000000), -1000000)