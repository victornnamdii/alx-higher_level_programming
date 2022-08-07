#!/usr/bin/python3
"""
File: test_base.py
Desc: This module contain unittest for models/base.py
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

import unittest
from models import base
import inspect
import pep8
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


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
        jstring = '[{"height": 4, "width": 10, "id": 89}, {"height": 7\
                , "width": 1, "id": 7}]'
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
