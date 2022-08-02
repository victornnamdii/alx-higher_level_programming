#!/usr/bin/python3
"""
File: 11-square.py
Desc: This module contains definition for the class Square
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""

R = __import__('9-rectangle').Rectangle


class Square(R):
    """
    Definition of class square that inherits from class Rectangle
    """

    def __init__(self, size):
        """
        Initializes instance of the class Square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns string representation of an instance of class square
        """
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)
