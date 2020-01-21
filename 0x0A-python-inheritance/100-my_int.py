#!/usr/bin/python3
"""
   Modulo: 100-my_int
   Description: modulo than invert eq and ne operators == & !=
"""


class MyInt(int):
    """
       Class: MyInt
       Description: Define Class MyInt
    """
    def __init__(self, value):
        """
           Function: __init__
           Description: init class function
        """
        self.value = value

    def __eq__(self, value):
        """
           Function: __eq__
           Description: invert == operator
        """
        return self.value != value

    def __ne__(self, value):
        """
           Function: __ne__
           Description: invert != operator
        """
        return self.value == value
