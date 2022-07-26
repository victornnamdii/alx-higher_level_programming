#!/usr/bin/python3
"""
File: 101-locked_class.py
Desc: This module contains one a class definition, LockedClass
Author: Ilodiuba Victor (victornnamdii)
Date Created: 26 Jul 2022
"""


class LockedClass:
    """
    This class prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute
    is called first_name
    """
    __slots__ = ["first_name"]
