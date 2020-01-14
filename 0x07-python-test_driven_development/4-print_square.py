#!/usr/bin/python3
"""
   Name Module: 4-print_square
   Description: Module that print a square whith the character #
"""


def print_square(size):
    """
       Name Function: print_square
       Description:prints in stdout the square with the character #
       @size:size of a square to print
       return: nothing
       error: raise TypeError if size is not integer
              raise ValueError if size is < 0
   """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
