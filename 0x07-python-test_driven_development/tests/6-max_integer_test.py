#!/usr/bin/python3
"""Unit test for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """unit test class for max_integer"""
    def test_module_docstring(self):
        """module docsting test"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """funstion docstring test"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """empty list [] test"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """Tests for no args passed"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for one element"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """Tests with max at end"""
        e = [6, 17, 9, 66, 64, 90]
        self.assertEqual(max_integer(e), 90)

    def test_positive_middle(self):
        """Tests with max in middle"""
        m = [1, 17, 9, 500, 64, 90]
        self.assertEqual(max_integer(m), 500)

    def test_positive_beginning(self):
        """Tests with max at beginning"""
        b = [1000, 17, 9, 66, 64, 90]
        self.assertEqual(max_integer(b), 1000)

    def test_one_negative(self):
        """Tests with one negative number"""
        on = [1000, 17, 9, -66, 64, 90]
        self.assertEqual(max_integer(on), 1000)

    def test_all_negative(self):
        """Tests with all negative numbers"""
        n = [-96, -90, -95, -1, -1000]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Test passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests with a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
