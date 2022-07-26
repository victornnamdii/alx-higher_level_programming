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
    def __setattr__(self, attr, value):
        """
        Checks if instance attribute is first_name
        """
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(attr))
        self.__dict__.update({attr: value})
