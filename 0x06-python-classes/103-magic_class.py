#!/usr/bin/python3
"""MagicClass module.

This module contains the MagicClass class used for the bytecode exercise.
"""


import math


class MagicClass():
    """Defines a MagicClass object."""

    def __init__(self, radius=0):
        """Sets the necessary attributes for the MagicClass object.

        Args:
            radius (int, float): the radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the current circle area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the current circle circumference."""
        return 2 * math.pi * self.__radius
