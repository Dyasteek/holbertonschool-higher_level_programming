#!/usr/bin/python3
"""Defining class rectangle"""


class Rectangle:
    """Empty class rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializing values and checking

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """

        setter for width

        Args: value (int): width of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if value != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """

        setter for height

        Args: value (int): height of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if value != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
