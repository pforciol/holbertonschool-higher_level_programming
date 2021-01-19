#!/usr/bin/python3
"""BaseGeometry module.

Contains a class BaseGeometry, and some methods.
"""


class BaseGeometry():
    """Defines the BaseGeometry class."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
