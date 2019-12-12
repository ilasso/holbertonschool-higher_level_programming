#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    size = len(sys.argv) - 1
    if size == 0:
        print("{:d} arguments.".format(size))
    elif size == 1:
        print("{:d} argument:".format(size))
    else:
        print("{:d} arguments:".format(size))
    while i < size:
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
        i += 1
