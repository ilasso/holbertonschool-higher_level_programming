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
