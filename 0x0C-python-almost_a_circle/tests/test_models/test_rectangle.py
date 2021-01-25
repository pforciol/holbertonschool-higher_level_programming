#!/usr/bin/python3
"""This is the rectangle.py unittest module."""
from unittest import TestCase, mock
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_basics(TestCase):
    """Test cases for Rectangle initialization."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_missing(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_Rectangle_only_required(self):
        self.assertEqual(Rectangle(2, 4).id, 1)
        self.assertEqual(Rectangle(4, 2).id, 2)

    def test_Rectangle_width_height_x(self):
        self.assertEqual(Rectangle(2, 4, 1).id, 1)
        self.assertEqual(Rectangle(4, 2, 2).id, 2)

    def test_Rectangle_no_id(self):
        self.assertEqual(Rectangle(2, 4, 1, 2).id, 1)
        self.assertEqual(Rectangle(4, 2, 2, 1).id, 2)

    def test_Rectangle_with_id(self):
        self.assertEqual(Rectangle(2, 4, 1, 2, 4).id, 4)
        self.assertEqual(Rectangle(4, 2, 2, 1, 2).id, 2)

    def test_width_get_set(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertEqual(r.width, 2)
        r.width = 42
        self.assertEqual(r.width, 42)

    def test_height_get_set(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__height
        self.assertEqual(r.height, 4)
        r.height = 42
        self.assertEqual(r.height, 42)

    def test_x_get_set(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__x
        self.assertEqual(r.x, 1)
        r.x = 42
        self.assertEqual(r.x, 42)

    def test_y_get_set(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__y
        self.assertEqual(r.y, 2)
        r.y = 42
        self.assertEqual(r.y, 42)


class Test_Rectangle_values(TestCase):
    """Test cases for Rectangle input, getter and setter values validation."""

    types = [
        None,
        "Betty Holberton",
        3.14,
        2j,
        ["Betty", "Holberton"],
        ("Betty", "Holberton"),
        range(42),
        {"first": "Betty", "last": "Holberton"},
        {"Betty", "Holberton"},
        frozenset({"Betty", "Holberton"}),
        True,
        b"Betty Holberton",
        bytearray(42),
        memoryview(bytes(42))
    ]

    def test_width_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "width must be an integer"):
                    Rectangle(type, 4)

    def test_width_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-42, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_height_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "height must be an integer"):
                    Rectangle(2, type)

    def test_height_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -42)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_x_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Rectangle(2, 4, type)

    def test_x_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -42)

    def test_y_invalid_type(self):
        for type in self.types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Rectangle(2, 4, 0, type)

    def test_y_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 0, -42)


class Test_Rectangle_area(TestCase):
    """Test cases for Rectangle's area method."""

    def test_area_basic(self):
        self.assertEqual(Rectangle(2, 4).area(), 8)

    def test_area_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).area(42)


class Test_Rectangle_display(TestCase):
    """Test cases for Rectangle's display method."""

    def test_display_basic(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4).display()
            self.assertEqual(output.getvalue(), '##\n##\n##\n##\n')

    def test_display_with_x(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2).display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n  ##\n  ##\n')

    def test_display_with_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 0, 2).display()
            self.assertEqual(output.getvalue(), '\n\n##\n##\n##\n##\n')

    def test_display_with_x_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2, 2).display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n  ##\n  ##\n')

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).display(42)


class Test_Rectangle_str(TestCase):
    """Test cases for Rectangle's __str__ method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_print(self):
        expected = "[Rectangle] (42) 1/3 - 2/4"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Rectangle(2, 4, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(), expected)

    def test_str_str_method(self):
        expected = "[Rectangle] (98) 3/1 - 4/2"
        self.assertEqual(Rectangle(4, 2, 3, 1, 98).__str__(), expected)

    def test_str_str(self):
        expected = "[Rectangle] (1) 0/0 - 4/4"
        self.assertEqual(str(Rectangle(4, 4)), expected)

    def test_str_str_method_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).__str__(42)


class Test_Rectangle_update_with_args(TestCase):
    """Test cases for Rectangle's update with *args method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_no_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")

    def test_update_args_none_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def test_update_args_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def test_update_args_id_width(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def test_update_args_id_width_height(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def test_update_args_id_width_height_x(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20, 30)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def test_update_args_id_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(24, 10, 20, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def test_update_args_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(10, 10, 10, 10, 10, 50, 60)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")


class Test_Rectangle_update_with_kwargs(TestCase):
    """Test cases for Rectangle's update with **kwargs method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_kwargs_none_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def test_update_kwargs_id(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def test_update_kwargs_id_width(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=40, width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def test_update_kwargs_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, id=10, x=10, height=10, betty="holberton")
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_mixed_too_many_args(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, width=10, betty="holberton", id=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_args_before(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(42, 42, 42, y=10, x=10)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 42/42")

    def test_update_kwargs_not_all_mixed(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(y=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (42) 10/10 - 2/10")

    def test_update_kwargs_only_wrong_keys(self):
        r = Rectangle(2, 4, 1, 2, 42)
        r.update(betty="holberton", holberton="betty")
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")


class Test_Rectangle_to_dict(TestCase):
    """Test cases for Rectangle's to_dictionary method."""

    def test_to_dictionary_basic(self):
        r = Rectangle(2, 4, 1, 2, 42)
        expected = {'width': 2, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        self.assertDictEqual(r.to_dictionary(), expected)

    def test_to_dictionary_basic_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
