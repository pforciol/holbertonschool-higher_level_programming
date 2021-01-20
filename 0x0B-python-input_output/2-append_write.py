#!/usr/bin/python3
"""append_write module.

Contains a function that appends a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    """
    with open(filename, 'a') as f:
        return f.write(text)
