#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxi = 0
    best = None
    for i, j in a_dictionary.items():
        if j > maxi:
            maxi = j
            best = i
    return best
