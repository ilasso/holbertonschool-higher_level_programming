#!/usr/bin/python3
"""
   Name Module: 1-rectangule
   Description: Module that define Class that defines a rectangle
"""


class Rectangle:
    """
       Name Class: Rectangle
       Description: define a Rectangle Class
    """
    def __init__(self, width=0, height=0):
        """
           Name Function: __init__
           Description:define and initialize private attributes
           @width: width of rectangle
           @height: heightof rectangle
           Error: width not int or < 0,
                  height not in or <0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
           Name Function: width getter
           Description: return object atribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
           Name Function: width setter
           Description: modify object atribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
           Name Function: height getter
           Description: return object atribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
           Name Function: height setter
           Description: modify object atribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
           Name Function: area
           Description:calculate area of rectangle
           Return: instance rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
           Name Function: perimeter
           Description:calculate perimeter of rectangle
           Return: instance rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
           Name Function: __str__
           Description: to print rectangle class whith str function
           Return: rep string rectangel whith character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        displayclass = []
        for i in range(0, self.__height):
            displayclass.append("#")
            for j in range(1, self.__width):
                displayclass.append("#")
                if j == (self.__width - 1) and i < self.__height - 1:
                    displayclass.append("\n")
        return "".join(displayclass)

    def __repr__(self):
        """
           Name Function: __repr__
           Description: return a string representation of the rectangle
                        to be able to recreate a new instance
        """
        width = self.__width
        height = self.__height
        return "Rectangle({}, {})".format(str(width), str(self.height))

    def __del__(self):
        """
           Name Function:__del__
           Description: execute when del instance
        """
        print("Bye rectangle...")
