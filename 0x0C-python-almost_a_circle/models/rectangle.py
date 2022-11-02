#!/usr/bin/python3
""" A class called Rectangle that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """ A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization method
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: horizontal position
            y: vertical position
            id: identity
        """
        self.width = width
        self.height = height
        self.x = x
        self. y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for the width
        Returns:
            the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height
        Returns:
            the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x
        Returns:
            the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y
        Returns:
            the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
