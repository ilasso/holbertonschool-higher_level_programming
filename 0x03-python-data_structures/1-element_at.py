#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx <= size and idx >= 0:
        return my_list[idx]
    else:
        return None
