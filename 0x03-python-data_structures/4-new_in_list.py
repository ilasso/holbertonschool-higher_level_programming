#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_my_list = []
    if idx < size and idx >= 0:
        for i in my_list:
            new_my_list.append(i)
        new_my_list[idx] = element
    return new_my_list
