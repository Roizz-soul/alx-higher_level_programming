#!/usr/bin/python3
"""Function for listing out available attributes and methods 
    of an instance"""


def lookup(obj):
    """lookup lists the attributes and methods of obj
    Returns:
        the list
    """
    return dir(obj)
