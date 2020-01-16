#!/usr/bin/python3
"""
   Name Module: 101-locked_class.
   Description: Module prevents the user from dynamically creating new instance
                attributes, except if the new instance attribute
                is called first_nam
"""


class LockedClass:
    """
       Name Class: LockedClass.
       Description: Class prevents the user from dynamically creating
                    new instance attributes, except if the new instance
                    attribute is called first_name
    """

    __slots__ = ["first_name"]
