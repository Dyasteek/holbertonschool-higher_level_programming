#!/usr/bin/python3

class Base(object):
    """Base: Class define base"""
    __nb_objcts = 0
    
    def __init__(self, id=None):
        """__init__ initialized constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objcts += 1
            self.id = Base.__nb_objcts