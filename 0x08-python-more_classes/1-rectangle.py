#!/usr/bin/python3
"""
Defines an class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initializes the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            """ sets the value for the width """
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
