#!/usr/bin/python3
"""Max integer test module.

This module contains a class that tests for the max_integer function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test function"""

    def test_max_integer(self):
        """
        Tests if correct tests are ok
        """
        lst = [1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)
        lst = [1, 4, 2, 3, -4]
        self.assertEqual(max_integer(lst), 4)
        lst = [4]
        self.assertEqual(max_integer(lst), 4)
        lst = [None]
        self.assertEqual(max_integer(lst), None)
        lst = []
        self.assertEqual(max_integer(lst), None)
        lst = [1, 3, float('inf'), 2]
        self.assertEqual(max_integer(lst), float('inf'))
        lst = [1, 3, -float('inf'), 2]
        self.assertEqual(max_integer(lst), 3)
        lst = [4, 1, 2, 3]
        self.assertEqual(max_integer(lst), 4)

    def test_type(self):
        """
        Tests if failure tests are ok
        """
        lst = [1, 2, 3, "Betty"]
        self.assertRaises(TypeError, max_integer, lst)
        lst = None
        self.assertRaises(TypeError, max_integer, lst)
