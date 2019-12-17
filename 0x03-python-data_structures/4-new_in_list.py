#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_my_list = []
    for i in my_list:
        new_my_list.append(i)
    if idx < size and idx >= 0:
        new_my_list[idx] = element
    return new_my_list
