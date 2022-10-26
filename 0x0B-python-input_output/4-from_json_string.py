#1/usr/bin/python3
"""using json representation"""
import json


def from_json_string(my_str):
    """using json format
    Args:
        my_obj: json string to be changed
    Returns:
        the python data structure format of my_str
    """
    return json.loads(my_obj)
