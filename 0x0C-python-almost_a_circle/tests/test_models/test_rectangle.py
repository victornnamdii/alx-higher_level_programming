#!/usr/bin/python3
""""
Unittest for rectangle module.
Test cases for Rectangle class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """A test class created to run tests for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_rec_inherit(self):
        '''Test if rectangle inherits from Base'''
        self.assertEqual(issubclass(Rectangle, Base), True)


if __name__ == '__main__':
    unittest.main()
