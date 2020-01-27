#!/usr/bin/python3
""" Module:Square"""
from models.base import Base
from models.rectangle import Rectangle
import sys


class Square(Rectangle):
    """ Class:Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Function:__init__"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Function:__str__
            Return: string representation class Square
        """
        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                   self.y, self.width)
        return string

    @property
    def size(self):
        """ Function:getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """ Function:setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Function:update"""
        if len(list(args)) > 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for i in kwargs.items():
                if i[0] == "id":
                    self.id = i[1]
                elif i[0] == "size":
                    self.size = i[1]
                elif i[0] == "x":
                    self.x = i[1]
                elif i[0] == "y":
                    self.y = i[1]
