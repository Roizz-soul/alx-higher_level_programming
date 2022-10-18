#!/usr/bin/python3
"""A function to print a square of Hashtags"""


def print_square(size):
    """print_square prints a square of hashtags
    Args:
        size: the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
