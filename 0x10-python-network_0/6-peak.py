#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def getPeak(array, inic, end):
    """main process, use recursion to find peak using binary search"""
    if inic == end:
        return array[inic]
    mid = int((inic + end) / 2)
    if array[mid] < array[mid + 1]:
        return getPeak(array, mid + 1, end)
    return getPeak(array, inic, mid)


def find_peak(list_of_integers):
    """find_peak: return one of peak of a unsorted integers list"""
    if not list_of_integers:
        return
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[1] <= list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return getPeak(list_of_integers, 0, len(list_of_integers) - 1)
