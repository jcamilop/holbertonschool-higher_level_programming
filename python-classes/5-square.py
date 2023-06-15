#!/usr/bin/python3
"""Make Square"""


class Square:
    """Represent Square """

    def __init__(self, size=0):
        """private square"""
        self.__size = size

    @property
    def size(self):
        """size return"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """inirializes square"""
        try:
            ("{:d}".format(value))
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except Exception:
            raise TypeError("size must be an integer")

    def area(self):
        """public square"""
        return(self.__size * self.__size)

    def my_print(self):
        """print square"""
        size = self.__size

        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print('#', end="")
                print()
