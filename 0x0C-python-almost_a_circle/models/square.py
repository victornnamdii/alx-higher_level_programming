#!/usr/bin/python3
"""
File: square.py
Desc: This module contains a class; Square
Author: Ilodiuba Victor (victornnamdii)
Date Created: 05 Aug 2022
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Implementation of the class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of the object
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        String representation of the class
        """
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.size))

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = self.height = value
