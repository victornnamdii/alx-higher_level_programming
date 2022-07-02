#!/usr/bin/python3
def no_c(my_string):
    nstring = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            nstring += c
    return(nstring)
