#!/usr/bin/python3
"""define a square"""


class Square:
    """ Make a square """

    def __init__(self, size=0):
        """private square"""
        self.__size = size

    def area(self):
        """public square"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """return size square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size square attribute"""
        try:
            ("{:d}".format(value))
            self.__size = value
        except Exception:
            raise TypeError("size must be an integer")
