#!/usr/bin/python3
"""MyList module.

Contains a class MyList that inherits from list
and a method that prints the sorted list.
"""


class MyList(list):
    """Defines the MyList class."""

    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
