#!/usr/bin/python3
"""Inheriting from another module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits methods from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle
        Args:
            width: width
            height: height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
