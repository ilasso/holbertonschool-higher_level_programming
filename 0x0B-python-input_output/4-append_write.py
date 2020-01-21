#!/usr/bin/python3
"""
   Name Module: 4-append_write
   Description: Module that create and append a file
   Functions: append_write
"""


def append_write(filename="", text=""):
    """
       Name function: append_write
       Description: create a file and append text string
                    if doesnt exits it create
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
    f.close()
