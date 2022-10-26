#1/usr/bin/python3
"""using json representation"""
import json


def to_json_string(my_obj):
    """using json format
    Args:
        my_obj: object to be changed
    Returns:
        the json format of my_obj
    """
    return json.dumps(my_obj)
