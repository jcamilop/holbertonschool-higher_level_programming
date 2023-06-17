#!/usr/bin/python3
"""Module 6-rectangle"""


class Rectangle:
    """clase rectangulo con base y altura"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instancia de rectangulo
        width - altura del rectangulo
        height - base del rectangulo
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """Dibujar una instancia de rectangulo"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Borrar instancia de un rectangulo"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Obtiene el ancho del rectangulo"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Establecer ancho del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el ancho del rectangulo"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Establecer ancho del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retornar area del rectangulo"""
        return self.__width * self.__height

    def perimeter(self):
        """Retornar perimetro del rectangulo"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
