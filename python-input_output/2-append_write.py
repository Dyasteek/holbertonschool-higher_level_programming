#!/usr/bin/python3
"""A function that appends a string to a text file"""


def append_write(filename="", text=""):
    """appending a string to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
