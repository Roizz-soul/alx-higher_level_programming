#!/usr/bin/python3
"""A class called base"""
import json


class Base:
    """Base class with no args
    Attributes:
        __nb_objects: a private class attribute number
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method
        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """java script object notation
        Args:
            list_dictionaries: a list o dictionaries
        Returns:
            JSON string interpretation
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to file(cls, list_objs):
        """javascript object notation
        Args:
            list_objs: list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
