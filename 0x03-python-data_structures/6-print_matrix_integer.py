#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        sizerow = len(i) - 1
        k = 0
        for j in i:
            if k == sizerow:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=" ")
            k += 1
