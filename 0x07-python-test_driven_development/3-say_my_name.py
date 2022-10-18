#!/usr/bin/python3
""" A function to print full name"""


def say_my_name(first_name, last_name=""):
    """Prints a full name
    Args:
        first_name: the first name, a string
        last_name: surname, also a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
