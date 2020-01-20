#!/usr/bin/python3
"""
   Name Module: 0-lookup.
   Description: Module that returns the list of available attributes 
                and methods of an object
"""
def lookup(ob):
    """
       Name Functions: Loockup.
       Description: returns the list of available attributes and 
                    methods of an object
    """
    return dir(ob)
