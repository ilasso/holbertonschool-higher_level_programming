#!/usr/bin/python3
"""
   Name Module: 8-load_from_json_file
   Description: Module that creates an Object from a “JSON file”
   Functions: save_to_json_file
"""
import json


def load_from_json_file(filename):
    """
       Name function: load_from_json_file
       Description: Function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
