#!/usr/bin/python3
"""Define a class square."""


class Square:
    """This class is about a square"""
    def __init__(self, size=0):
        """Initializing each new square.

        Args:
            size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """A getter to return the size of the square

        Returns:
            The size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter to chenge the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Instance/Object method that calculates the area of square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)
