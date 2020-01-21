#!/usr/bin/python3
"""
   Name Module: 3-is_kind_of_class
   Description: Module returns True if the object is an instance of,
                or if the object is an instance of a class that inherited from,
                the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
       Name Functions: is_kind_of_class
       Description: returns True if the object is an instance of, or if the
                    object is an instance of a class that inherited from,
                    the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
