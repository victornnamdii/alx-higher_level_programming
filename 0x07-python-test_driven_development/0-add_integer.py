#!/usr/bin/python3
"""
File: 0-add_integer.py
Desc: This module supplies one function, add_integer(a, b)
Author: Ilodiuba Victor (victornnamdii)
Date Created: Jul 23 2022
"""


def add_integer(a, b=98):
    """
    This function computes the addition of two numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
