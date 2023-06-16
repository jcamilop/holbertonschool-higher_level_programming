#!/usr/bin/python3
"""module for import matrix_divided """


def matrix_divided(matrix, div):
    """divides the numbers of a matrix"""
    # for div
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # for matrix
    if not matrix or type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    len_r = 0
    for elements in matrix:
        if not elements or type(elements) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len_r != 0 and len(elements) != len_r:
            raise TypeError("Each row of the matrix must have the same size")

        mensaje = "matrix must be a matrix (list of lists) of integers/floats"
        for numero in elements:
            if not type(numero) in (int, float):
                raise TypeError(mensaje)
        len_r = len(elements)

    new_m = list(
        map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (new_m)
