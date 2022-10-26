#!/usr/bin/python3
"""Using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """putting the json rep in a file
    Args:
        my_obj: python object to be converted
        filename: name of file to be written into
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
