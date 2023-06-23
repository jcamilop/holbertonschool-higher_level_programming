#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Represent class"""

    def area(self):
        """Make exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide int"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
