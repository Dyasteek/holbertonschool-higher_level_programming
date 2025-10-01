#!/usr/bin/python3
"""A function that reads a text file and prints it to stdout"""

def read_file(filename=""):
    """printing the content of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
