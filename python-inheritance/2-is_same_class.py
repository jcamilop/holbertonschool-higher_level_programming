#!/usr/bin/python3
"""If the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """same class"""
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
