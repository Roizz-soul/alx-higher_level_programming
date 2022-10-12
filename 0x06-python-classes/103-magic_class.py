#!/usr/bin/python3
import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initialize a MagicClass

        Args:
            radius: The radius of the class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the area of the MagicClass.

        Reuturns:
            chwck code
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """The circumference of the MagicClass.

        Returns:
            check code
        """
        return (2 * math.pi * self.__radius)
