#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        imax = my_list[0]
        for i in my_list:
            if i > imax:
                imax = i
        return imax
    return None
