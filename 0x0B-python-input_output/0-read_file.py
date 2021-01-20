#!/usr/bin/python3
"""read_file module.

Contains a function that reads a text file.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
