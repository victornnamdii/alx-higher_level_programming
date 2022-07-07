#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    hold = []
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            hold.append(keys)
    for keys in hold:
        del a_dictionary[keys]
    return(a_dictionary)
