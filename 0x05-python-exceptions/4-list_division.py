#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            result = 0
            print("wrong type")
            pass
        except ZeroDivisionError:
            result = 0
            print("division by 0")
            pass
        except IndexError:
            result = 0
            print("out of range")
            pass
        finally:
            newlist.append(result)
    return newlist
