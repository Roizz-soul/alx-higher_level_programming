#!/usr/bin/python3
"""Unitest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def tests_lists(self):
        """Tests the lists for max"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([1.5, 2.3, 3.6, 4.2]), 4.2)
        self.assertAlmostEqual(max_integer(["name", "is", "Book"]), "name")

    if __name__ == '__main__':
        unittest.main
