#!/usr/bin/python3
"""modulo for importr read file"""


def read_file(filename=""):
    """Read a text file and print it to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
