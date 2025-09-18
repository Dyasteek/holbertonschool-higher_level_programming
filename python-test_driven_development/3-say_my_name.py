#!/usr/bin/python3
"""
a function that prints My name is <name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <name> <last name>

    Raises:
        TypeError: if arguments are not strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
