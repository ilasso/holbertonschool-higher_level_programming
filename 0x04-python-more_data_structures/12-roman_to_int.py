#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romandic = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                     ('C', 100), ('D', 500), ('M', 1000)])
    number = 0
    size = len(roman_string) - 1
    for i, j in enumerate(roman_string):
        number += romandic.get(j)
    if romandic.get(roman_string[i]) > romandic.get(roman_string[i-1]):
        number -= (romandic.get(roman_string[i]) +
                   romandic.get(roman_string[i-1]))
        number += (romandic.get(roman_string[i]) -
                   romandic.get(roman_string[i-1]))
    return number
