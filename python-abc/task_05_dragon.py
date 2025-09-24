#!/usr/bin/env python3
"""Dragon class demonstrating mixins"""


class SwimMixin:
    """Mixin class that provides swimming functionality"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin"""

    def roar(self):
        print("The dragon roars!")
