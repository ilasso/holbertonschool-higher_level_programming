#!/usr/bin/python3
""" Module: base """

import json

class Base:
    """ Class: Base"""
    _nb_objects = 0

    def __init__(self, id=None):
        """ Function: __init__
            args: id
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    def to_json_string(list_dictionaries):
        """ Function: to_json_string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
   
