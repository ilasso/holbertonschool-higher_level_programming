#!/usr/bin/python3
"""
   Name Module: 3-write_file
   Description: Module that create a file
   Functions: write_file
"""


def write_file(filename="", text=""):
    """
       Name function: write_file
       Description: create a file with text string if doesnt exits it create
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
    f.close()
