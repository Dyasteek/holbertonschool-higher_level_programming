#!/usr/bin/python3
"""
a function that prints a text 2 lines after each of: . ? and :
"""


def text_indentation(text):
    """
    prints a text 2 lines after each of: . ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[i])
            print()
        else:
            print(text[i], end="")
