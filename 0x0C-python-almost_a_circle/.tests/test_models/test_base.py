#!/usr/bin/python3
"""
File: test_base.py
Desc: This module contain unittest for models/base.py
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""
import os
from models.rectangle import Rectangle
from models.square import Square
import unittest
from models import base
import inspect
Base = base.Base


class TestBase(unittest.TestCase):
    """
    Unit tests for the base model
    """

    def test_id_init(self):
        """
        Testing id initialization
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        b3 = Base(70)
        self.assertEqual(b3.id, 70)
        b4 = Base()
        self.assertEqual(b4.id, b2.id + 1)

    def test_json_method(self):
        """tests Base's to_json_string method
        """
        r1 = Rectangle(4, 5, 6, 7, 8)
        r2 = Rectangle(10, 11, 12, 13, 14)
        dictionary = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary, d2])
        j_d = eval(json_dict)
        self.assertEqual(j_d[0]['id'], 8)
        self.assertEqual(j_d[1]['x'], 12)

    def test_create_inst(self):
        """
        Testing create method
        """
        r = Rectangle(9, 2, 3, 4, 45)
        s = Square(4, 8, 9, 2)
        r_d = r.to_dictionary()
        s_d = s.to_dictionary()
        r2 = Rectangle.create(**r_d)
        s2 = Square.create(**s_d)
        self.assertEqual(s.id, s2.id)
        self.assertEqual(r.id, r2.id)
        self.assertEqual(s.y, s2.y)
        self.assertEqual(s.x, s2.x)
        self.assertEqual(r.width, r2.width)
        self.assertEqual(s.size, s2.size)

    def test_read_from_file(self):
        """tests the base class method read from file, for use in
            -> Rectangle and Square
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_read_from_file_basic(self):
        """tests the base class method to read from json files when
            -> input is basic
        """
        r1 = Rectangle(10, 7, 8, 3, 44)
        r2 = Rectangle(24, 23, 5, 1, 99)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        rects = Rectangle.load_from_file()
        self.assertEqual(rects[0].width, 10)
        self.assertEqual(rects[1].id, 99)
        self.assertEqual(rects[1].x, 5)

    def test_write_csv_basic(self):
        """tests the base class method to write instances as csv
        """
        r1 = Rectangle(10, 7, 2, 8, 33)
        r2 = Rectangle(10, 8, 4, 9, 44)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r', encoding='utf-8') as myFile:
            text = myFile.readlines()
        self.assertEqual(text[0][0] + text[0][1], "33")
        self.assertEqual(text[1][0] + text[1][1], "44")

    def test_read_csv_basic(self):
        """tests the base class method to read from csv
            -> basic input
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(8, list_output[0].y)
        self.assertEqual(4, list_output[1].height)
        self.assertEqual(4, list_output[1].height)

    def test_read_csv_empty(self):
        """
        Testing read csv
        """
        try:
            os.remove('Square.csv')
        except Exception:
            pass
        list_output = Square.load_from_file_csv()
        self.assertEqual(0, len(list_output))
        self.assertEqual(list, type(list_output))

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
