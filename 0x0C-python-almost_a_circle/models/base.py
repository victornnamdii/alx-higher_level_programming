#!/usr/bin/python3
"""
File: base.py
Desc: THis module contains a class; Base
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""


class Base:
    """
    Representation of the class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
