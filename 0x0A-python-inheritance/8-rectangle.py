#!/usr/bin/python3
"""Rectangle module.

Contains a class Rectangle that inherits
from BaseGeometry and some methods.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """constructor for Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
