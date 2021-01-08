#!/usr/bin/python3
"""
This is the matrix_mul module.

This module supplies one function, matrix_mul().
"""


def matrix_mul(m_a, m_b):
    """
    Return a new matrix multiplied.

    Args:
        m_a (list): list of lists of integers or floats.
        m_b (list): list of lists of integers or floats.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) > 0:
        for row_a in m_a:
            if len(row_a) is 0:
                raise ValueError("m_a can't be empty")
    else:
        raise ValueError("m_a can't be empty")
    if len(m_b) > 0:
        for row_b in m_b:
            if len(row_b) is 0:
                raise ValueError("m_b can't be empty")
    else:
        raise ValueError("m_b can't be empty")

    for row_a in m_a:
        for i in row_a:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row_b in m_b:
        for i in row_b:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    row_a_len = 0
    for row_a in m_a:
        if len(row_a) is not row_a_len and row_a_len is not 0:
            raise TypeError("each row of m_a must be of the same size")
        row_a_len = len(row_a)
    row_b_len = 0
    for row_b in m_b:
        if len(row_b) is not row_b_len and row_b_len is not 0:
            raise TypeError("each row of m_b must be of the same size")
        row_b_len = len(row_b)

    if row_a_len is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)] for row_a in m_a]
