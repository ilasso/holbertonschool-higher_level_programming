#!/usr/bin/python3
"""
   Name Module: 10-square
   Description: Module that that inherits from Rectangle (9-rectangle.py)
   Functions: area
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
           Name function: __init__
           Description: init subclase Square and superclase Rectangle
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
           Name function: area
           Description:return Square area
        """
        return self.__size * self.__size
