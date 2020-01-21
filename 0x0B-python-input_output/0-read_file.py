#!/usr/bin/python3
"""
   Name Module: 0-read_file
   Description: Module that read a text file
   Functions: read_file
"""


def read_file(filename=""):
    """
       Name function: read_file
       Description: read all text file
    """
    with open(filename, encoding='utf-8') as f:
        for i in f:
            print(i, end="")
    f.close()
