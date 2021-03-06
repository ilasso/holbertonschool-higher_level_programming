#!/usr/bin/python3
"""
   Name Module: 14-pascal_triangle
   Description: define function pascal_traingle
"""


def pascal_triangle(n):
    """
        Name function: pascal_triangle
        Description: return matrix pascal
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle_list = [[1], [1, 1]]
    for i in range(1, n-1):
        triangle_row = [1]
        for j in range(0, len(triangle_list[i])-1):
            element = triangle_list[i][j] + triangle_list[i][j+1]
            triangle_row.extend([element])
        triangle_row += [1]
        triangle_list.append(triangle_row)
    return triangle_list
