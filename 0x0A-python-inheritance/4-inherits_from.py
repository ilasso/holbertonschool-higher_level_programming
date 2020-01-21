#!/usr/bin/python3
"""
   Name Module:4-inherits_from
   Description: Module returns True if the object is an instance of a class
                that inherited (directly or indirectly) from the specified
                class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
       Name Function: inherits_from
       Description: returns True if the object is an instance of a class
                    that inherited (directly or indirectly) from the specified
                    class ; otherwise False
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    return False
