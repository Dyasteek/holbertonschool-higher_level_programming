#!/usr/bin/env python3
"""CountedIterator class that extends built-in iterator functionality"""


class CountedIterator:
    """CountedIterator class that extends the built-in iterator"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return next(self.iterator)
