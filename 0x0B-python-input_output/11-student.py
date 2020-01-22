#!/usr/bin/python3
"""
   Name Module: 11-student
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

    def to_json(self):
        """
            Name function: to_json
            Description: returns the dictionary description with simple
                         data structure
                         (list, dictionary, string, integer and boolean)
                         for JSON serialization of an object
        """
        return self.__dict__
