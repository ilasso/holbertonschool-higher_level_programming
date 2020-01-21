#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
       Name Class: Rectangle
       Description: inherits from BaseGeometry. validate width and height
                    whith integer_validator
    """
    def __init__(self, width, height):
        """
           Name function: __init__
           Description: init subclase Rectablge
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
