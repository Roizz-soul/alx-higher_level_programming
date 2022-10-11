#!/usr/bin/python3
"""Define a class square."""


class Square:
    """This class is about a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing each new square.

        Args:
            size: size of the new square
            position: bkdjhf
        """
        self.__position = position
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

    @property
    def position(self):
        """A getter to return the size of the square

        Returns:
            The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A setter for position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple
                                of 2 positive integers")
            if i < 0:
                raise TypeError("position must be a tuple
                                of 2 positive integers")
        self.__position = value

    def area(self):
        """Instance/Object method that calculates the area of square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """A my_print method to print a square"""
        if self.__size == 0:
            print()
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print("_" * self.__position[0], end="")
            print("#" * self.__size)
