#!/usr/bin/python3
""" Module:Rectangle """
from models.base import Base
import sys


class Rectangle(Base):
    """ Class:Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Function:__init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Function:getter width"""
        return self.__width

    @property
    def height(self):
        """ Function:getter height"""
        return self.__height

    @property
    def x(self):
        """ Function:getter x"""
        return self.__x

    @property
    def y(self):
        """ Function:getter y"""
        return self.__y

    @width.setter
    def width(self, width):
        """ Function:setter width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Function:setter height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("heightmust be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ Function:setter x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ Function:setter y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Function:area
            Return: area of rectangle
        """
        return self.width * self.height

    def display(self):
        """ Function:display
            Return: draw rectangle with # char
        """
        for k in range(0, self.y):
            print()
        for i in range(0, self.height):
            for l in range(0, self.x):
                print(" ", end="")
            print("#", end="")
            for j in range(1, self.width):
                print("#", end="")
                if j == (self.width - 1):
                    print()
        if self.width == 1:
            print()

    def __str__(self):
        """ Function:__str__
            Return: string representation class rectangle
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                         self.y, self.width,
                                                         self.height)
        return string

    def update(self, *args, **kwargs):
        """ Function:update
            Return: assign an argument to each attribute
        """
        if len(list(args)) > 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                else:
                    self.y = args[i]
        else:
            for i in kwargs.items():
                if i[0] == "id":
                    self.id = i[1]
                elif i[0] == "width":
                    self.width = i[1]
                elif i[0] == "height":
                    self.height = i[1]
                elif i[0] == "x":
                    self.x = i[1]
                elif i[0] == "y":
                    self.y = i[1]
