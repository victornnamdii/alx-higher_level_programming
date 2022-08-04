#!/usr/bin/python3
"""
File: test_rectangle.py
Desc: This module contains unittest for rectangle.py
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

from io import StringIO
import unittest
from unittest.mock import patch
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle

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
        out1 = "##\n##\n"
        out2 = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r12.display()
            self.assertEqual(fake_out.getvalue(), out1)
            r13.display()
            self.assertEqual(fake_out.getvalue(), out1 + out2)

    def test_str(self):
        """
        Testing string representation
        """
        r14 = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r14)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

if __name__ == '__main__':
    unittest.main()
