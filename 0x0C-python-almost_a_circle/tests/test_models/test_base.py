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
        b1 = Base()
        b2 = Base()
        b3 = Base(70)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 70)
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()
