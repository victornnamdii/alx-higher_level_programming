#!/usr/bin/python3
"""
File: 8-rectangle.py
Desc: This module contains a class Rectangle
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""
G = __import__('7-base_geometry').BaseGeometry


class Rectangle(G):
    """
    A class Rectangle inherited from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
