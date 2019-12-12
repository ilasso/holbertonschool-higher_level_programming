#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    suma = 0
    size = len(sys.argv) - 1
    while i < size:
        suma += int(sys.argv[i + 1])
        i += 1
    print("{:d}".format(suma))
