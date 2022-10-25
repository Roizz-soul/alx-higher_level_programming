#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:
    """Raises error for now"""
    def area(self):
        """raises an exception of no implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks for the value and type of *value*
        Args:
            name: a string
            value: an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
