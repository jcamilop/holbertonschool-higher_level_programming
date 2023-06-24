#!/usr/bin/python3
"""Module for pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        prev_row = [0] + triangle[-1] + [0]
        temp = []
        for j in range(len(triangle[-1]) + 1):
            temp.append(prev_row[j] + prev_row[j + 1])
        triangle.append(temp)
    return (triangle)
