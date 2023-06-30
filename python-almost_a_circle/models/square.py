#!/usr/bin/python3
"""class Square import class Rectangle"""
from models.rectangle import Rectangle


"""Create class Square"""


class Square(Rectangle):
    """Create constructor for square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """print constructor"""

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """Getter for square"""
    @property
    def size(self):
        return self.width

    """setter for square"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """Adding update function with arguments"""

    def update(self, *args, **kwargs):
        """print dimensions of the print rectangle"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    """adding dictionary in the square"""

    def to_dictionary(self):
        """create dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
