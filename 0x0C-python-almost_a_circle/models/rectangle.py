#!/usr/bin/python3
"""
File: rectangle.py
Desc: This module contains a class; Rectangle
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

from models.base import Base


class Rectangle(Base):
    """
    Representation of the class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        String representation of class
        """
        return ("[Rectangle] (" +
                str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) +
                " - " + str(self.__width) + "/" + str(self.__height))

    def check_value(self, name, value, sides=True):
        """
        Checks if correct input was inserted
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if sides:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value for width
        """
        self.check_value('width', value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value for height
        """
        self.check_value('height', value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value for x
        """
        self.check_value('x', value, False)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value fo y
        """
        self.check_value('y', value, False)
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'
        """
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width) + '\n', end='')

    def update(self, *args, **kwargs):
        """
        Updates the attributes values
        """
        if len(args):
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
