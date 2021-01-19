#!/usr/bin/python3
"""MyInt module.

Contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """Defines the MyInt class."""

    def __eq__(self, other):
        """Sets the == behaviour."""
        return int(self) != other

    def __ne__(self, other):
        """Sets the != behaviour."""
        return int(self) == other
