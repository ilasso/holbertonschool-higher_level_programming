#!/usr/bin/python3
"""
   Name Module: 14-pascal_triangle
   Description: define function pascal_traingle
"""


def pascal_triangle(n):
    """
        Name function: pascal_triangle
        Description: init  class Student
    """
    triangle_list = [[1], [1, 1]]
    for i in range(1, n):
        triangle_row = [1]
        for j in range(0, len(triangle_list[i])-1):
            triangle_row.extend([triangle_list[i][j] + triangle_list[i][j+1]])
        triangle_row += [1]
        triangle_list.append(triangle_row)
    return triangle_list
