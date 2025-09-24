#!/usr/bin/python3
"""A class MyList that inherits from list and prints in asc order"""


class MyList(list):
    """A class inheriting from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list in asc order"""
        print(sorted(self))
