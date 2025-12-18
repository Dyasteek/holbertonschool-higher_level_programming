#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only those attributes are retrieved
        Otherwise, all attributes are retrieved"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                if attrs is None or key in attrs:
                    result[key] = value
        return result
