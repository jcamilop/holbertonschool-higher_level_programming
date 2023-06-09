#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    return [list(map(lambda num: num ** 2, i)) for i in matrix]
