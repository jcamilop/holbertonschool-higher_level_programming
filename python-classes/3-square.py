#!/usr/bin/python3
"""Class Square """


class Square:
    """ Class square"""

    def __init__(self, size=0):
        """ Parameter: size of square"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Public instance method"""
        return (self.__size * self.__size)
