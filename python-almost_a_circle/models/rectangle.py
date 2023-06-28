#!/usr/bin/python3
"""Module Rectangle"""

import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @property
    def x(self):
        """Get coordinate x of Rectangle"""
        return self.__x

    @property
    def y(self):
        """Get cordinate y of Rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """atribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """atribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """atribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """atribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of Rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """print rectangle instance whit #"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of Rectangle instance"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.height
        st = (
            f"[Rectangle] ({i}) {x}/{y} - {w}/{h}")
        return (st)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        assigns a key/value argument to attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) == 2:
                self.width = args[1]
            if len(args) == 3:
                self.height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dic_r = {"y": self.__y, "x": self.__x,
                                "id": self.id, "width": self.__width,
                 "height": self.__height}
        return (dic_r)
