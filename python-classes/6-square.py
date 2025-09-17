#!/usr/bin/python3
"""Class Square"""


class Square:
    """Private instance"""

    def __init__(self, size=0, position=(0, 0)):
        """Init the size of square

        Args:
            size (int): size of square
            position (tuple): position of square
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
        if position != (int(position[0]), int(position[1])):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area calculator"""
        return self.__size ** 2

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        """Atribute init

        Args:
            value (int): size of square
        """
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position

        Args:
            value (tuple): position of square
        """
        if value != (int(value[0]), int(value[1])):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print with #"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
        return
