#!/usr/bin/python3
"""A class called base"""


class Base:
    """Base class with no args
    Attributes:
        __nb_objects: a private class attribute number
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method
        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
