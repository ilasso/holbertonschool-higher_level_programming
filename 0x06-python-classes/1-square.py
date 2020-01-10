#!/usr/bin/python3
"""
   Name Module: 1-Square.
   Description: Module that define Square Class with private atrribute (size)
"""


class Square():
    """
       Name Class: Square.
       Description: define a private attribute
    """
    def __init__(self, size):
        """
           Name Function: __init__
           Description:define and initialize private attribute
                       with a value arg
        """
        self.__size = size
