#!/usr/bin/python3
"""This is the peak module."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): the list of integers to find the peak in.
    """

    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    half = int(length / 2)
    peak = list_of_integers[half]
    if peak > list_of_integers[half - 1] and peak > list_of_integers[half + 1]:
        return peak
    elif peak > list_of_integers[half + 1]:
        return find_peak(list_of_integers[:half])
    else:
        return find_peak(list_of_integers[half + 1:])
