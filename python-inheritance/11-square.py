#!/usr/bin/python3
"""Square Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """New square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String for pint the rectangle"""
        return str(f"[Square] {self.__size}/{self.__size}")

    def area(self):
        """Return area"""
        return (self.__size * self.__size)
