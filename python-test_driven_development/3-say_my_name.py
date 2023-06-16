#!/usr/bin/python3
"""
Module for import say my name
"""


def say_my_name(first_name, last_name=""):
    """
    return a string with both names
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
