#!/usr/bin/python3
"""A class that defines a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""
    def __init__(self, width, height):
        """A method that initializes the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        