#!/usr/bin/env python3
"""FlyingFish class demonstrating multiple inheritance"""


class Fish:
    """Fish class with swim and habitat methods"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat methods"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
