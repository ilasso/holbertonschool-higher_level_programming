#!/usr/bin/python3
"""
   Name Module: 10-class_to_json
   Description: returns the dictionary description with simple
                data structure
                (list, dictionary, string, integer and boolean)
                for JSON serialization of an object
"""


def class_to_json(obj):
    """
       Name function: class_to_json
       Description: returns the dictionary description with simple
                    data structure
                    (list, dictionary, string, integer and boolean)
                    for JSON serialization of an object
    """
    return obj.__dict__
