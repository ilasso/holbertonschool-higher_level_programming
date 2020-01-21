#!/usr/bin/python3
"""
   Name Module: 1-MyList.
   Description: Module that prints a list sorted
"""


class MyList(list):
    """
       Name Class: My list
       Description: define a My list class
    """
    def print_sorted(self):
        """
           Name Functions: print_sorted
           Description: returns the list sorted
        """

        print(sorted(self))
