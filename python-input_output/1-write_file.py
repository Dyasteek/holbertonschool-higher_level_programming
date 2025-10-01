#!/usr/bin/python3
"""mamaco"""


def write_file(filename="", text=""):
    """writing a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
