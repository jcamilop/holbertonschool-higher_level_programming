#!/usr/bin/python3
"""Write a class hat inherits from list """


class MyList(list):
    """list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
