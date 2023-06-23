#!/usr/bin/python3
"""Module for import write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Return the number of characters"""
    with open(filename, 'w+') as f:
        return f.write(text)
