#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if size > 0 and idx <= size and idx > 0:
        my_list.remove(my_list[idx])
    return my_list
