#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
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

    def test_type(self):
        lst = [1, 2, 3, "Betty"]
        self.assertRaises(TypeError, max_integer, lst)
        lst = None
        self.assertRaises(TypeError, max_integer, lst)
