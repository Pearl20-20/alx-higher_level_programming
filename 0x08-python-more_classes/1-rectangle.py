#!/usr/bin/python3
"""Declaring an empty class"""


class Rectangle:
    """creating a Rectangle  Class
    with Width and Heigth as its properties"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """getter property for width"""
    def width(self):
        return self.__width

    @width.setter
    """setter property for width that
    checks is Value is an integer or negative"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """getter property for height"""
    def height(self):
        return self.__height

    @height.setter
    """setter property for heigth  that
    checks is Value is an integer or negative"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
