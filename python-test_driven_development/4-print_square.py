#!/usr/bin/python3
""" Modulo for import print square"""


def print_square(size):
    """ Picture a square of size int and mor tan 0 """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
