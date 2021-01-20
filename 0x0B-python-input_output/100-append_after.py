#!/usr/bin/python3
"""write_file module.

Contains a function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after
    each line containing a specific string.
    """
    with open(filename, 'r') as f:
        content = f.readlines()

    for i in range(len(content) + 2):
        if search_string in content[i]:
            content.insert(i + 1, new_string)

    with open(filename, 'w') as f:
        for line in content:
            f.write(line)
