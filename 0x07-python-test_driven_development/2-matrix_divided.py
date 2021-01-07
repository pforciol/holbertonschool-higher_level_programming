#!/usr/bin/python3
"""
This is the matrix_divided module.

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.

    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): the divider, >= 0.
    """
    mtrx_type_e = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_len_e = 'Each row of the matrix must have the same size'
    div_type_e = 'div must be a number'
    div_zero_e = 'division by zero'

    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_e)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_e)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_e)
        if len(row) is not row_len and row_len is not 0:
            raise TypeError(mtrx_len_e)
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError(div_type_e)
    if div is 0:
        raise ZeroDivisionError(div_zero_e)

    return [[round(nb / div, 2) for nb in row] for row in matrix]
