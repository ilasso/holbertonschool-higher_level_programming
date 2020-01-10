#!/usr/bin/python3
"""
   Name Module: 3-Square.
   Description: Module that define Square Class with private atrribute (size)
"""


class Square():
    """
       Name Class: Square.
       Description: define a private attribute
    """
    def __init__(self, size=0):
        """
           Name Function: __init__
           Description:define and initialize private attribute
                       with a value arg.
                       if arg not integer raise typerro
                       if arg < 0 raise value error
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
           Name Function: area
           Description:define and initialize private attribute
                       with a value arg.
                       if arg not integer raise typerro
                       if arg < 0 raise value error
                       calculate square area and return value
        """
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size * self.__size
