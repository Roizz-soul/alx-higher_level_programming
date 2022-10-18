#!/usr/bin/python3
"""A function to multiply matrices"""


def matrix_mul(m_a, m_b):
    """matrix_mul multiplies two matrices
    Args:
        m_a: First matrix of ints or floats
        m_b: Second matrix of ints or floats
    Returns:
        A new matrix, the multiplied result
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not isinstance(row, list) for row in m_a:
        raise TypeError("m_a must be a list")
    if not isinstance(tow, list) for tow in m_b:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if type(elem) not in [int, float] for elem in [row for row in m_a]:
        raise TypeError("m_a should contain only integers or floats")
    if type(elems) not in [int, float] for elems in [tow for tow in m_b]:
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a:
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(tow) == len(m_b[0]) for tow in m_b:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    new_row = []
    inverted_b = []
    for r in range(len(m_b[0]):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    for row in m_a:
        new_row = []
        for el in inverted_b:
            prod = 0
            for i in ranger(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        result.append(new_row)

    return result
            
