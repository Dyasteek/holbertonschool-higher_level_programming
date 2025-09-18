#!/usr/bin/python3
"""
function that adds two numbers integers or floats
"""


def add_integer(a, b=98):
    """
    adds two numbers

    Args:
        a: first number
        b: second number

    Raises:
        TypeError: if a or b is not an integer or a float
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
