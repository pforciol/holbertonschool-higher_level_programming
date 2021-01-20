#!/usr/bin/python3
"""class_to_json module.

Contains a function that returns a dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    """
    return obj.__dict__
