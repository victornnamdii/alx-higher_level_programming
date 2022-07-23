#!/usr/bin/python3
"""
File: 2-matrix_divided.py
Desc: This module contains one function matrix_divided(matrix, div)
Author: Ilodiuba Victor (victornnamdii)
DAte Created: 23 Jul 2022
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    """
    if not(type(matrix) == list and matrix != [] and
            all(type(row) == list for row in matrix) and
            all(type(e) in [float, int] for e in [e
                for row in matrix for e in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
