#!/usr/bin/python3

class Base:
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialized constructor"""
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
