#!/usr/bin/python3
"""
File: 3-say_my_name.py
Desc: This module contains one function: say_my_name(first_name, last_name="")
Author: Ilodiuba Victor (victornnamdii)
Date Created: 23 Jul 2022
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
