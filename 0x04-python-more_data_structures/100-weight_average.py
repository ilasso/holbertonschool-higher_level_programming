#!/usr/bin/python3
def weight_average(my_list=[]):
    suma = 0
    count = 0
    for i, j in enumerate(my_list):
        suma += j[0] * j[1]
        count += j[1]
    return suma / count
