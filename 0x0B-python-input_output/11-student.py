#!/usr/bin/python3
"""Student module.

Contains a Student class and some methods.
"""


class Student():
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets the necessary attributes for the Student object.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for k, v in json.items():
            setattr(self, k, v)
