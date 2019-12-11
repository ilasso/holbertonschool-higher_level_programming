#!/usr/bin/python3
def uppercase(str):
    i = 0
    l = len(str)
    while i < l:
        if ord(str[i]) in range(97, 123):
            char = chr(ord(str[i]) - 32)
        else:
            char = chr(ord(str[i]))
        print("{}".format(char), end="")
        i += 1
    print()
