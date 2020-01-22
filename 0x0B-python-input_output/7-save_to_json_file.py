#!/usr/bin/python3
"""
   Name Module: 7-save_to_json_file
   Description: Module that writes an Object to a text file,
                using a JSON representation
   Functions: save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
       Name function: save_to_json_file
       Description: Function that writes an Object to a text file,
                using a JSON representation
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
