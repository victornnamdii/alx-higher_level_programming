#!/usr/bin/python3
"""
File: 100-matrix_mul.py
Desc: This module contains one function, matrix_mul(m_a, m_b)
Author: Ilodiuba Victor (victornnamdii)
Date Created: 25 Jul 2022
"""


def matrix_mul(m_a, m_b):
    """
    This function computes matrix multiplication
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not(all(type(row) == list for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not(all(type(row) == list for row in m_b)):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a[0] == []:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b[0] == []:
        raise ValueError("m_b can't be empty")
    if not(all(type(e) in [float, int] for e in [e for row in m_a for e in
                                                 row])):
        raise TypeError("m_a should contain only integers or floats")
    if not(all(type(e) in [float, int] for e in [e for row in m_b for e in
                                                 row])):
        raise TypeError("m_b should contain only integers or floats")
    if not(all(len(row) == len(m_a[0]) for row in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if not(all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("each row of m_b must be of the same size")

    cm_a = len(m_a[0])
    rm_b = 0
    for row in m_b:
        rm_b += 1

    if cm_a != rm_b:
        raise ValueError("m_a and m_b can't be multiplied")
    answer = []
    for i in range(len(m_a)):
        inside = []
        for j in range(len(m_b[0])):
            c = 0
            for k in range(rm_b):
                c += (m_a[i][k] * m_b[k][j])
            inside.append(c)
        answer.append(inside)
    return answer
