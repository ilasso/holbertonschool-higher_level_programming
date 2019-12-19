#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        newrow = [x * x for x in i]
        newmatrix.append(newrow)
    return(newmatrix)
