#!/usr/bin/python3
"""Class Square"""


class Square:
    """Private instance"""

    def __init__(self, size=0):
        """Atribute init

        Args:
            size (int): size of square
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area calculator"""
        return self.__size ** 2
