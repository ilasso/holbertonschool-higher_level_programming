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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function: to_json_string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Function: save_to_file
        """
        listdict = []
        if list_objs is not None:
            for i in list_objs:
                listdict.append(i.to_dictionary())

        string = Base.to_json_string(listdict)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """ Function: from_json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
