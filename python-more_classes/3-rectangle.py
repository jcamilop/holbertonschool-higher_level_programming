#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle:
    """clase rectangulo con base y altura"""

    def __init__(self, width=0, height=0):
        """
        Instancia de rectangulo
        width - altura del rectangulo
        height - base del rectangulo
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ dibujar el rectangulo"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """obtiene la altura del rectangulo"""
        return self.__width

    @width.setter
    def width(self, value):
        """establecer altura del rectangulo"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Obtener base del rectangulo"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Establecer base del rectangulo"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retornar area del rectungulo"""
        return self.__width * self.__height

    def perimeter(self):
        """ Retornar perimetro del rectangulo """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)
