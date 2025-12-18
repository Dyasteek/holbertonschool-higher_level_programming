#!/usr/bin/python3
"""Module for converting class instance to JSON-serializable dictionary"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object"""
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
