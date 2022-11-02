#!/usr/bin/python3
"""A class called square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method
        Args:
            size: the size of the square
            x: horixontal position
            y: vertical position
            id: identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the width
        Returns:
            the width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Width Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """the string method
        Returns:
            a string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
