#!/usr/bin/python3
"""Dictionary description of an object"""


def class_to_json(obj):
    """dictionary description with simple data structure
    Returns:
        dict desc.
    """
    return obj.__dict__
