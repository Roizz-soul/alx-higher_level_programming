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

    def update(self, *args, **kwargs):
        """updating the parameters
        Args:
            *args: values to be changed
            *kwargs: key_worded arguments
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns dictionary representation fo the instance"""
        return {'id': self.id,
                'size': self.size
                'x': self.x,
                'y': self.y}

    def __str__(self):
        """the string method
        Returns:
            a string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
