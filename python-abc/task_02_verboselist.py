#!/usr/bin/env python3
"""VerboseList class that extends Python's list"""


class VerboseList(list):
    """VerboseList class that extends the built-in list class"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        length_before = len(self)
        super().extend(iterable)
        items_added = len(self) - length_before
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
