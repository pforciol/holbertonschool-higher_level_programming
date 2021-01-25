#!/usr/bin/python3
"""This is the Rectangle module.

Contains the Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from Base and defines a Rectangle object.

    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.
        __x (int): the horizontal (x) padding of the rectangle.
        __y (int): the vertical (y) padding of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object.

        Args:
            width (int): the wanted width of the rectangle.
            height (int): the wanted height of the rectangle.
            x (int): the wanted horizontal (x) padding of the rectangle.
            y (int): the wanted vertical (y) padding of the rectangle.
            id (int): the wanted identifier of the Base object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # width attribute getter and setter.
    @property
    def width(self):
        """Get and Set the width attribute of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height attribute getter and setter.
    @property
    def height(self):
        """Get and Set the height attribute of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x attribute getter and setter.
    @property
    def x(self):
        """Get and Set the x attribute of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y attribute getter and setter.
    @property
    def y(self):
        """Get and Set the y attribute of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Methods
    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates the Rectangle attributes.

        Args:
            args (list): attributes to be modified [id, width, height, x, y].
            kwargs (dict): attributes to be modified.
        """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == 'id' and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }
