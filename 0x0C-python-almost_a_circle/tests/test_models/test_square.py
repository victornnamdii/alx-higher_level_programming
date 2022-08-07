#!/usr/bin/python3
"""
File: test_square.py
Desc: This module contains unittest for Square
Author: Ilodiuba Victor (victornnamdii)
Date Created: 05 Aug 2022
"""

import pep8
import inspect
from io import StringIO
import unittest
from unittest.mock import patch
from models import square
from models.rectangle import Rectangle
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """Tests the Square class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """Test that models/square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """
    Unit test for Square module
    """

    def test_id(self):
        """
        Testing id initialization
        """
        s1 = Square(5)
        self.assertEqual(s1.id, Base._Base__nb_objects)
        s2 = Square(2, 2)
        self.assertEqual(s2.id, Base._Base__nb_objects)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, Base._Base__nb_objects)

    def test_size(self):
        """
        Testing self initialization
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(2, 2)
        self.assertEqual(s2.size, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)

    def test_area(self):
        """
        Testing the area method
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_x(self):
        """
        Testing x setter
        """
        s1 = Square(2, 7)
        self.assertEqual(s1.x, 7)

    def test_y(self):
        """
        Testing y setter
        """
        s1 = Square(4, 1, 3)
        self.assertEqual(s1.y, 3)

    def test_height_width(self):
        """
        Testing width and height value
        """
        s1 = Square(7, 8, 9)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)

    def test_str_and_update(self):
        """
        Testing string representation of square
        and update method
        """
        out1 = "[Square] (1) 0/0 - 2\n"
        out2 = "[Square] (2) 4/0 - 3\n"
        out3 = "[Square] (3) 5/6 - 4\n"
        s1 = Square(5)
        s1.update(1, 2)
        s2 = Square(2, 2)
        s2.update(2, 3, 4)
        s3 = Square(3, 1, 3)
        s3.update(3, 4, 5, 6)
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            print(s2)
            print(s3)
            self.assertEqual(f.getvalue(), out1 + out2 + out3)
        s1.update(size=17, x=9, y=7, id=98)
        out1 = "[Square] (98) 9/7 - 17\n"
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            self.assertEqual(f.getvalue(), out1)

    def test_display(self):
        """
        Testing display method
        """
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        out1 = "#####\n#####\n#####\n#####\n#####\n"
        out2 = "  ##\n  ##\n"
        out3 = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s1.display()
            s2.display()
            s3.display()
            self.assertEqual(f.getvalue(), out1 + out2 + out3)

    def test_value_validation(self):
        """
        Tests the Exceptions
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(5, "b")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s2 = Square(5, -7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(5, 7, "b")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s2 = Square(5, 8, -7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("b")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s2 = Square(0)

    def test_dictionary(self):
        """
        Tests the to_dictionary method
        """
        s1 = Square(10, 2, 1)
        s1.update(1)
        hold = s1.to_dictionary()
        self.assertEqual(hold, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s2 = Square(1, 1)
        s2.update(**hold)
        self.assertEqual(s1.size, s2.size)
        self.assertFalse(s1 == s2)
        self.assertIs(type(hold), dict)


if __name__ == '__main__':
    unittest.main()
