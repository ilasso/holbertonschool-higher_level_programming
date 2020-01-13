#!/usr/bin/python3
"""
2-matrix_divided: module to divide values of a simetrical number lists of list
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: function that divide all values into a list of list
    @matrix : list of list to process
    @div: number to divide current values of a list
    return: similar list whith values divided by div
    Error: TypeError: number of a list should be int or floats
           div should be a int or
           all rows of a list should be have same size
           ZeroDivisionError: div should be float and not zero
    """

    if div is None:
        raise TypeError("div must be a number")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = list.__len__(matrix[0])
    newmatrix = []
    for i, j in enumerate(matrix):
        if len(j) == 0:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if type(j) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if size != len(j):
            raise TypeError("Each row of the matrix must have the same size")
        newmatrix.append([])
        for l, k in enumerate(j):
            if (type(j) != list) or ((type(k) != int) and (type(k) != float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            newmatrix[i].append(round((k/div), 2))
    return newmatrix
