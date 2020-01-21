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
        raise Exception("area() is not implemented")
