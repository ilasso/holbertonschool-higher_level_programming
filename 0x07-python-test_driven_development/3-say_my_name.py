#!/usr/bin/python3
"""
3-say_my_name: module print a name composed by first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: function print a name composed by first and last name
    @first_name : first name to print
    @last_name: last name to print
    return: northing
    Error: firts_name is not string
           last_name is not string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
