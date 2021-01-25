#!/usr/bin/python3
"""This is the base.py unittest module."""
from unittest import TestCase
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base_ID(TestCase):
    """Test cases for Base id."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_ID_empty(self):
        self.assertEqual(Base().id, 1)

    def test_ID_none(self):
        self.assertEqual(Base(None).id, 1)

    def test_ID_positive(self):
        self.assertEqual(Base(42).id, 42)

    def test_ID_negative(self):
        self.assertEqual(Base(-42).id, -42)

    def test_ID_mixed(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(42).id, 42)
        self.assertEqual(Base(None).id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(-42).id, -42)


class Test_Base_to_json_string(TestCase):
    """Test cases for to_json_string static method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_string_type(self):
        r = Rectangle(2, 4, 1, 2, 42)
        s = Square(2, 1, 2, 42)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        dicts = [r.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 53)

    def test_to_json_string_basic_square(self):
        s = Square(2, 1, 2, 42)
        dicts = [s.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 39)

    def test_to_json_string_multiple_dicts(self):
        r = Rectangle(2, 4, 1, 2, 42)
        s = Square(2, 1, 2, 42)
        dicts = [r.to_dictionary(), s.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dicts)) == 92)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_None_list(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 42)


class Test_Base_save_to_file(TestCase):
    """Test cases for save_to_file static method."""

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_save_to_file_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_basic_square(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file([s])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_multiple_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_multiple_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 78)

    def test_save_to_file_overwrite(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file([s])
        s = Square(42, 42, 42, 42)
        Square.save_to_file([s])
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 42)


class Test_Base_from_json_string(TestCase):
    """Test cases for from_json_string static method."""

    def test_from_json_string_type(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_basic_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_basic_square(self):
        list_input = [{'id': 89, 'size': 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_rectangles(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 98, 'width': 1, 'height': 8}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_square(self):
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 98, 'size': 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_multiple_empty(self):
        self.assertEqual([], Base.from_json_string('[]'))

    def test_from_json_string_multiple_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_multiple_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 42)


class Test_Base_create(TestCase):
    """Test cases for create static method."""

    def test_create_basic_rectangle(self):
        dct = {'width': 2, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        r = Rectangle.create(**dct)
        self.assertDictEqual(r.to_dictionary(), dct)

    def test_create_basic_square(self):
        dct = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        s = Square.create(**dct)
        self.assertDictEqual(s.to_dictionary(), dct)


class Test_Base_load_from_file(TestCase):
    """Test cases for load_from_file static method."""

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_load_from_file_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_load_from_file_no_file(self):
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_from_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(42)


class Test_Base_save_to_file_csv(TestCase):
    """Test cases for save_to_file_csv static method."""

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.csv")
        except:
            pass
        try:
            os.remove("Square.csv")
        except:
            pass

    def test_save_to_file_csv_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '42,2,4,1,2\n')

    def test_save_to_file_csv_basic_square(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '42,2,1,2\n')

    def test_to_json_string_csv_multiple_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), '42,2,4,1,2\n24,4,2,2,1\n')

    def test_to_json_string_csv_multiple_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '42,2,1,2\n24,4,2,1\n')

    def test_save_to_file_csv_overwrite(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file_csv([s])
        s = Square(42, 42, 42, 42)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), '42,42,42,42\n')

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], 42)


class Test_Base_load_from_file_csv(TestCase):
    """Test cases for load_from_file_csv static method."""

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_csv_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file_csv([r1, r2])
        lst = Rectangle.load_from_file_csv()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_load_from_file_csv_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file_csv([s1, s2])
        lst = Square.load_from_file_csv()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_load_from_file_csv_no_file(self):
        lst = Rectangle.load_from_file_csv()
        self.assertEqual(lst, [])

    def test_load_from_file_csv_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv(42)


if __name__ == "__main__":
    unittest.main()
