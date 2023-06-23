#!/usr/bin/python3
"""class BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representate a square"""

    def __init__(self, size):
        """New square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area"""
        return (self.__size * self.__size)
