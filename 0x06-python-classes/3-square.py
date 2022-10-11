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

    def area(self):
        """Instance/Object method that calculates the area of square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)
