#!/usr/bin/python3
"""
   Name Module: 5-to_json_string.py
   Description: Module that create and append a file
   Functions: append_write
"""
import json


def to_json_string(my_obj):
    """
       Name function: to_json_string
       Description:function that returns the JSON representation
                   of an object (string):
    """
    return json.dumps(my_obj)
