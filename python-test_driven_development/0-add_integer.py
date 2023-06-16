#!/usr/bin/python3
"""
Module by a function for add two numbers

"""


def add_integer(a, b=98):
    """
    Function that adds two integer and/or float numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a + b))
