#!/usr/bin/python3
"""
Unittest for base module.
Test cases for base class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """A test class created to run tests for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0_id_None(self):
        '''Test for id with None argument passed'''
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_1_id(self):
        '''Test to check for id'''
        b1 = Base()
        b2 = Base()
        b3 = Base(11)
        b4 = Base(-12)
        b5 = Base(0)
        b6 = Base(1.1)
        b7 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 11)
        self.assertEqual(b4.id, -12)
        self.assertEqual(b5.id, 0)
        self.assertEqual(b6.id, 1.1)
        self.assertEqual(b7.id, 3)

    def test_2_id_single(self):
        '''Test for single instance creation with id'''
        b1 = Base(3)
        self.assertEqual(b1.id, 3)

    def test_3_id_multi(self):
        '''Test for multiple instance creation with id'''
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        b2 = Base(4)
        self.assertEqual(b2.id, 4)

    def test_4_id_string(self):
        '''Test for string argument'''
        b1 = Base("foo")
        self.assertEqual(b1.id, "foo")

    def test_5_id_NaN(self):
        '''Test for NaN as argument'''
        b1 = Base(float("nan"))
        self.assertNotEqual(b1.id, float("nan"))

    def test_6_id_sameId(self):
        '''Test for same ids'''
        b1 = Base(22)
        self.assertEqual(b1.id, 22)
        b2 = Base(22)
        self.assertEqual(b2.id, 22)


if __name__ == '__main__':
    unittest.main()
