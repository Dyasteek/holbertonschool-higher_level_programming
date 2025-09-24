#!/usr/bin/python3
"""An empty class"""


class BaseGeometry:
    """An empty class"""
    def area(self):
        """An empty method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
