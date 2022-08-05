#!/usr/bin/python3
"""
File: test_base.py
Desc: This module contain unittest for models/base.py
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unit tests for the base model
    """

    def test_id_init(self):
        """
        Testing id initialization
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(70)
        self.assertEqual(b3.id, 70)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_from_json_string(self):
        """
        Testing from_json_string method
        """
        jstring = '[{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]'
        jlist = Base.from_json_string(jstring)
        self.assertIs(type(jlist), list)
        self.assertEqual(len(jlist), 2)
        self.assertIs(type(jlist[0]), dict)
        self.assertIs(type(jlist[1]), dict)
        hold1 = {'height': 4, 'width': 10, 'id': 89}
        hold2 = {'height': 7, 'width': 1, 'id': 7}
        self.assertEqual(hold1, jlist[0])
        self.assertEqual(hold2, jlist[1])

if __name__ == '__main__':
    unittest.main()
