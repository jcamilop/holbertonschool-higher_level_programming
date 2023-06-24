#!/usr/bin/python3
"""Student class"""


class Student:
    """Make student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""

        dict_s = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    dict_s.update({x: self.__dict__[x]})
            return dict_s
        return self.__dict__.copy()
