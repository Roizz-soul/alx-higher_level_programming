#!/usr/bin/python3
"""A class with ref to json"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialization method
        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary rep.
        Args:
            attrs: a list of strings
        Returns:
            dict. rep.
        """
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
