#!/usr/bin/python3
"""
File: test_rectangle.py
Desc: This module contains unittest for rectangle.py
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

import pep8
import inspect
from io import StringIO
import unittest
from unittest.mock import patch
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """
    Unit test for Rectangle
    """
    def test_rectangle_id(self):
        """
        Testing rectangle id
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)
        r3 = Rectangle(10, 2, 0, 0, 98)
        self.assertEqual(r3.id, 98)
        r4 = Rectangle(8, 9)
        self.assertEqual(r4.id, Rectangle._Base__nb_objects)

    def test_exceptions(self):
        """
        Testing exceptions
        """
        r5 = Rectangle(10, 2)
        r6 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r7 = Rectangle(10, "2")
            r5.width = -10
            r6.x = {}
            r8 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """
        Testing area
        """
        r9 = Rectangle(3, 2)
        r10 = Rectangle(2, 10)
        r11 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r9.area(), 6)
        self.assertEqual(r10.area(), 20)
        self.assertEqual(r11.area(), 56)

    def test_display(self):
        """
        Testing display
        """
        r12 = Rectangle(2, 2)
        r13 = Rectangle(4, 6)
        r15 = Rectangle(3, 2, 1, 0)
        r16 = Rectangle(2, 3, 2, 2)
        out1 = "##\n##\n"
        out2 = "####\n####\n####\n####\n####\n####\n"
        out3 = " ###\n ###\n"
        out4 = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r12.display()
            self.assertEqual(fake_out.getvalue(), out1)
            r13.display()
            self.assertEqual(fake_out.getvalue(), out1 + out2)
            r15.display()
            self.assertEqual(fake_out.getvalue(), out1 + out2 + out3)

        with patch('sys.stdout', new=StringIO()) as f:
            r16.display()
            self.assertEqual(f.getvalue(), out4)

    def test_str(self):
        """
        Testing string representation
        """
        r14 = Rectangle(4, 6, 2, 1, 12)
        out3 = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r14)
            self.assertEqual(fake_out.getvalue(), out3)

    def test_update(self):
        """
        Testing update method
        """
        r17 = Rectangle(10, 10, 10, 10)
        out1 = "[Rectangle] (89) 10/10 - 10/10\n"
        out2 = "[Rectangle] (89) 10/10 - 2/3\n"
        out3 = "[Rectangle] (89) 4/5 - 2/3\n"
        out4 = "[Rectangle] (89) 4/5 - 2/1\n"
        out5 = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as f:
            r17.update(89)
            print(r17)
            self.assertEqual(f.getvalue(), out1)
            r17.update(89, 2, 3)
            print(r17)
            self.assertEqual(f.getvalue(), out1 + out2)
            r17.update(89, 2, 3, 4, 5)
            print(r17)
            self.assertEqual(f.getvalue(), out1 + out2 + out3)

        with patch('sys.stdout', new=StringIO()) as f:
            r17.update(height=1)
            print(r17)
            self.assertEqual(f.getvalue(), out4)
            r17.update(x=1, height=2, y=3, width=4)
            print(r17)
            self.assertEqual(f.getvalue(), out4 + out5)

    def test_dictionary(self):
        """
        Testing to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1.update(1)
        hold = r1.to_dictionary()
        self.assertEqual(hold,
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        r2.update(**hold)
        self.assertEqual(r1.y, r1.y)
        self.assertFalse(r1 == r2)
        self.assertIs(type(hold), dict)

    def test_to_json_string(self):
        """
        Testing the base static method to_json_string
        """
        r1 = Rectangle(10, 7, 2, 8)
        r1.update(1)
        hold = r1.to_dictionary()
        json_dict = Base.to_json_string([hold])
        self.assertEqual(hold,
                         {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertIs(type(json_dict), str)

    def test_create(self):
        """
        Testing the create method
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
