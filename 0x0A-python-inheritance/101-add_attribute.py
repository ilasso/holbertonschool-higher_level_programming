#!/usr/bin/python3
"""
   Modulo: 101-add_attribute
   Description: module create an attribute if cant raise
"""


def add_attribute(object, nameatr, valueatr):
    """
       Function: add_attribute
       Description: create an attribute
                        if cant raise can't add new attribute
    """
    if hasattr(object, "__dict__"):
        setattr(object, nameatr, valueatr)
        return
    raise TypeError("can't add new attribute")
