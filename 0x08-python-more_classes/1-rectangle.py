#!/usr/bin/python3


class Rectangle:
    """
    Set the propetits of the rectangle
    width - The vertical distance of the rectangle
    height -  Horizontal distance of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """property for width"""
    def width(self):
        return self.__width

    @width.setter
    """checks if the value passed is an Interger or not negative"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """property for height"""
    def height(self):
        return self.__height

    @height.setter
    """checks if the value passed is an Interger or not negative"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
