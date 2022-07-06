#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    total = 0
    for i in unique:
        total += i
    return(total)
