#!/usr/bin/python3
"""
Module that contains 1 simple classes : Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Simple rectangle class"""

    def __init__(self, width, height):
        """ Init method for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
