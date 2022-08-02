#!/usr/bin/python3
"""
File: 5-save_to_json_file.py
Desc: This module contains one function; save_to_json_file(my_obj, filename)
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
