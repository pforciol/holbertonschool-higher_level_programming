#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square and init method that
sets its size and checking if the given values are right.

"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.

        Raises:
            TypeError: if size is not given as an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
