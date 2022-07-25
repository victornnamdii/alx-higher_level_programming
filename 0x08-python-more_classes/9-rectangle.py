#!/usr/bin/python3
"""
Defines an class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with equal sides """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ defines the string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i < (self.__height - 1):
                print()
        return ""

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Defines action when rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
