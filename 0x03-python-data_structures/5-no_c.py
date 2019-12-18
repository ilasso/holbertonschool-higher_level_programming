#!/usr/bin/python3
def no_c(my_string):
    string = list(my_string)
    for i in my_string:
        if i == 'c' or i == 'C':
            string.remove(i)
    my_string = "".join(string)
    return my_string
