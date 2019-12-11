#!/usr/bin/python3
def islower(c):
    lowerlist = list(range(97, 123))
    if ord(c) in lowerlist:
        return True
    else:
        return False
