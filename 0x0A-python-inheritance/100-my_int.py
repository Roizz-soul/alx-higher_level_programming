#!/usr/bin/python3
"""A class that inherits from int"""


class MyInt(int):
    """Changing some builtin methods"""
    def __eq__(self, value):
        """change == to !=
        Returns:
            the changed thing
        """
        return self.real != value

    def __ne__(self, value):
        """change != to ==
        Returns:
            the changed thing
        """
        return self.real == value
