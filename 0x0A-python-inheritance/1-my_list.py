#!/usr/bin/python3
"""Class to show inheritance"""


class MyList(list):
    """Inherits methods and attributes from list"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
