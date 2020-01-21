#!/usr/bin/python3
"""
   Name Module: 5-base_geometry
   Description: Module that define a BaseGeometry
   Functions: area
"""


class BaseGeometry():
    """
       Name Class: BaseGeometry
       Description: raise an Exception whit the message
                    area() is not implemented
    """
    def area(self):
        """
           Name function: area
           Description: raise an Exception whit the message
                        area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
           Name function: integer_validator
           Description: raise an Exception whith the message
                        <name> must be an integer if no a integer
                        and
                        <name> mustbe greater than 0 if <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """
           Name function: area
           Description:return rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
           Name function: __str__
           Description:return rectangle area
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
