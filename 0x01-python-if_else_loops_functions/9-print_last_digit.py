#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = 0
    if number >= 0:
        lastdigit = number % 10
    elif number < 0:
        lastdigit = ((number * -1) % 10)
    print(lastdigit, end="")
    return lastdigit
