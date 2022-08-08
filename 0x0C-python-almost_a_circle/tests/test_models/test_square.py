#!/usr/bin/python3
"""
Unittest for square module.
Test cases for Square class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """A test class created to run tests for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_squ_inherit(self):
        '''Test if square inherits from Rectangle'''
        self.assertEqual(issubclass(Square, Rectangle), True)


if __name__ == '__main__':
    unittest.main()
