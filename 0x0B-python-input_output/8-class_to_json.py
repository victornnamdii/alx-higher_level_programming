#!/usr/bin/python3
"""
File: 8-class_to_json.py
Desc: This module contains one function; class_to_json(obj)
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    return obj.__dict__
