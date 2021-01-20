#!/usr/bin/python3
"""write_file module.

Contains a function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after
    each line containing a specific string.
    """
    out = ""
    with open(filename, 'r') as f:
        for line in f:
            out += line
            if search_string in line:
                out += new_string

    with open(filename, 'w') as f:
        f.write(out)
