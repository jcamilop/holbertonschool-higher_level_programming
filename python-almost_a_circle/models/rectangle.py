#!/usr/bin/python3
"""Define class rectangle"""


from models.base import Base


"""define class rectangle with base class"""


class Rectangle(Base):
    """define init in class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """get width"""

    @property
    def width(self):
        return self.__width

    """get height"""

    @property
    def height(self):
        return self.__height

    """get x"""

    @property
    def x(self):
        return self.__x

    """get y"""

    @property
    def y(self):
        return self.__y

    """setter width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """setter height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """setter x"""

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Setter y"""

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Adding Area to the rectangle"""

    def area(self):
        """Add a new area to the rectangle"""
        return self.__width * self.__height

    """Adding display # in the rectangle"""

    def display(self):
        """adding loops for the print rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    """Adding __str__ to the print rectangle"""

    def __str__(self):
        """print dimensions of the print rectangle"""
        dimensions = f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) " + dimensions

    """Update the print rectangle"""

    def update(self, *args, **kwargs):
        """print dimensions of the print rectangle"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    """adding dictionary in the rectangle"""

    def to_dictionary(self):
        """create dictionary"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
