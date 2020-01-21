#!/usr/bin/python3
"""
   Name Module: 2-read_lines
   Description: Module that read Q lines give by arg
   Functions: read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
       Name function: read_lines
       Description: read Qlines give by arg,
                    if Qlines is <= 0 or >= total file lines
                    prints all file otherwise print Qlines Only
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            f.seek(0)
            print(f.read(), end="")
        else:
            f.seek(0)
            for i in range(nb_lines):
                print(f.readline(), end="")
