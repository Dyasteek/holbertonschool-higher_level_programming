#!/usr/bin/python3
"""A class that defines a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size):
        """A method that initializes the square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """A method that returns the area of the square"""
        return self.__size ** 2
