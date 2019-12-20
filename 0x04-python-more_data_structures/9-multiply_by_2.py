#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicc = dict()
    dicc = a_dictionary.copy()
    for i, j in dicc.items():
        dicc[i] = j * 2
    return dicc
