#!/usr/bin/python3
""" Modulo for lookup
function that returns the list of available
ttributes and methods of an object"""


def lookup(obj):
    """return list"""
    return dir(obj)
