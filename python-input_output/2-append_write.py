#!/usr/bin/python3
"""import mudulo append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text of a file
    Return the number of characters"""
    with open(filename, 'a+') as f:
        return f.write(text)
