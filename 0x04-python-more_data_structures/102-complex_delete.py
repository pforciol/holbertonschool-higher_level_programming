#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in list(a_dictionary.items()):
        if v is value:
            a_dictionary.pop(k)
    return a_dictionary
