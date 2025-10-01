#!/usr/bin/python3
"""A function that returns the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """returning the JSON representation of an object"""
    return json.dumps(my_obj)
