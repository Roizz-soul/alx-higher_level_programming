#!/usr/bin/python3
"""loading from a json file"""
import json


def load_from_json_file(filename):
    """Create an object from a json file
    Returns:
        the created object
    """
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
