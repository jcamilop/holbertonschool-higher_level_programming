#!/usr/bin/python3
"""Define Rectangle from BaseGeometry"""


class BaseGeometry:
    """Represent class"""

    def area(self):
        """Make exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide int"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent rectangle"""

    def __init__(self, width, height):
        """Initiaize Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return (self.__width * self.__height)

    def __str__(self):
        """String for pint the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
