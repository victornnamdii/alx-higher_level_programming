#!/usr/bin/python3
"""defines a class called square"""


class Square:
    """Initialize a square
    Args:
        __size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        Args:
            size (int): size of the square
        Returns: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets for posution"""
        if (type(value) is tuple and len(value) == 2
                and type(value[0]) is int and type(value[1])
                is int and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """This computes the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for z in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __repr__(self):
        """defines the print representation of Square"""
        ret = ""
        if self.__size == 0:
            return ret
        for s in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i < (self.__size - 1):
                print("")
        return ret
