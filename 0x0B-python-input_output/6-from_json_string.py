#!/usr/bin/python3
"""
   Name Module: 6-from_json_string
   Description: Module that returns an object (Python data structure)
                represented by a JSON string
   Functions: from_json_string
"""
import json


def from_json_string(my_str):
    """
       Name function: from_json_string
       Description: Module that returns an object (Python data structure)
                    represented by a JSON string
    """
    return json.loads(my_str)
