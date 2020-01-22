#!/usr/bin/python3
"""
   Name Module: 13-student
   Description: define class Student
"""


class Student:
    """
       Name class:student
       Description: define class student
    """
    def __init__(self, first_name, last_name, age):
        """
            Name function: __init__
            Description: init  class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Name function: to_json
            Description: returns the dictionary description with simple
                         data structure
                         (list, dictionary, string, integer and boolean)
                         for JSON serialization of an object
                         If attrs is a list of strings, only attribute names
                         contained in this list must be retrieved.
                         Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        dicc = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dicc[i] = self.__dict__[i]
        return dicc

    def reload_from_json(self, json):
        """
            Name function: to_json
            Description: replaces all attributes of the Student instance
        """

        self.first_name = json.get('first_name')
        self.last_name = json.get('last_name')
        self.age = age = json.get('age')
