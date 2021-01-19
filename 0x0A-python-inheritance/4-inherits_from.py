#!/usr/bin/python3
"""inherits_from module.

Contains function that compares an object with an instance.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
