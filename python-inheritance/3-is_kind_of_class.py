#!/usr/bin/python3
"""the object is an instance of, or if the object is an
instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """check instance of a given class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
