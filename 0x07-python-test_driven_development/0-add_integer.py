#!/usr/bin/python3
"""
0-add_ingeger: module for add integer function
"""


def add_integer(a, b=98):
    """add_integer: Function that add two numbers
       @a: Firts number, shout be int or float
       @b: Second number, shout be int or float
       Error: if a or b not are integers or float
       return: add a + b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
