#!/usr/bin/python3
"""This is the Square module.

Contains the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle and defines a Square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object.

        Args:
            size (int): the size of a square side.
            x (int): the wanted horizontal (x) padding of the square.
            y (int): the wanted vertical (y) padding of the square.
            id (int): the wanted identifier of the Base object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    # size attribute getter and setter.
    @property
    def size(self):
        """Get and Set the size attribute of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    # Methods
    def update(self, *args, **kwargs):
        """Updates the Square attributes.

        Args:
            args (list): attributes to be modified [id, size, x, y].
            kwargs (dict): attributes to be modified.
        """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for i in range(len(args) if len(args) <= 4 else 4):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == 'id' and value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
