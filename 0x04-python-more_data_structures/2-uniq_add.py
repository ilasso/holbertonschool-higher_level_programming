#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for i in set(my_list):
        suma = suma + i
    return suma
