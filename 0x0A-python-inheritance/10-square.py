#!/usr/bin/python3
"""
File: 10-square.py
Desc: This module contains a class Square
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""

R = __import__('9-rectangle').Rectangle


class Square(R):
    """
    Definition of class Square that inherits from class Rectangle
    """

    def __init__(self, size):
        """
        Initialise an instance of the class Square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return the area of the square
        """
        return self.__size ** 2
