#!/usr/bin/python3
"""defines a class called square"""


class Square:
    """Initialize a square
    Args:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (int): size of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """getter of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value for size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This computes the area of the square"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """equality representation"""
        return self.__size == other.__size

    def __ne__(self, other):
        """not equal to representation"""
        return self.__size != other.__size

    def __gt__(self, other):
        """greater thanepresentation"""
        return self.__size > other.__size

    def __ge__(self, other):
        """greater than or equal to representation"""
        return self.__size >= other.__size

    def __lt__(self, other):
        """less than reprsentation"""
        return self.__size < other.__size

    def __le__(self, other):
        """less than or equal to representation"""
        return self.__size <= other.__size
