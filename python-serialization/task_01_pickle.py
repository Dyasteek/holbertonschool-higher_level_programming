#!/usr/bin/env python3
"""Custom object serialization using pickle"""
import pickle


class CustomObject:
    """Custom object with serialization capabilities"""
    
    def __init__(self, name, age, is_student):
        """Initialize CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Display object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
    
    def serialize(self, filename):
        """Serialize object to file using pickle"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file using pickle"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
