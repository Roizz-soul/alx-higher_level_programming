#!/usr/bin/python3
"""A class called square"""
from rectangle import Rectangle


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

    def __str__(self):
        """the string method
        Returns:
            a string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
