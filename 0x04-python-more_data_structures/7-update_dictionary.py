#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    dicc = dict()
    dicc[key] = value
    a_dictionary.update(dicc)
    return a_dictionary
