#!/usr/bin/python3
"""defines a class called square"""


class Square:
    """Initialize a square
    Args:
        __size (int): size of the square
    """
    def __init__(self, size):
        """Initialize a square
        Args:
            size (int): size of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
