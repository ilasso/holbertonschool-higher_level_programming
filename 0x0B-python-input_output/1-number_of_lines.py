#!/usr/bin/python3
"""
   Name Module: 1-number_of_lines
   Description: Module that read a text file
   Functions: number_of_lines
"""


def number_of_lines(filename=""):
    """
       Name function: number_of_lines
       Description: return number of lines a file
    """
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
