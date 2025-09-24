#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        return "Meow"
