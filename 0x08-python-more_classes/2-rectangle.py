#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle with height and width class"""
    def __init__(self, width=0, height=0):
        """ initialization method
        Args:
            width: width of rectangle (int)
            height: height of rectangle (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width
        Returns:
            the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width
        Args:
            value: new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height
        Returns:
            the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        Args:
            value: new value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area of the rectangle
        Returns:
            the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """the perimeter of the rectangle
        Returns:
            the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)
