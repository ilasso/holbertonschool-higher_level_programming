#!/usr/bin/python3
"""
   Name Module: 100-magic_string
   Description: Module that returns a string “Holberton” n times
                the number of the iteration
"""


def magic_string(lista=[]):
    """
      Name Function: magic_string
      Description: Returns a string “Holberton” n times
                   the number of the iteration
    """
    lista += ["Holberton"]
    return ", ".join(lista)
