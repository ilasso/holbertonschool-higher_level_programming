#!/usr/bin/python3
"""
   Name Module: 2-is_name_class
   Description: Module that returns True if the object
                is exactly an instance of the specified
"""


def is_same_class(obj, a_class):
    """
       Name Functions: is_same_class
       Description: function that returns True if the object is exactly
                    an instance of the specified
    """
    if type(obj) == a_class:
        return True
    return False
