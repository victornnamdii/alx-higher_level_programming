#!/usr/bin/python3
"""
File: 2-is_same_clas.py
Desc: This module contains one function; is_same_class
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""


def is_same_class(obj, a_class):
    """
    Returns true if object is exactly an instance of
    specified class, otherwise False
    """
    return isinstance(obj, a_class)
