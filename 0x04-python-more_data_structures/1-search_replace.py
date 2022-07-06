#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = [replace if my_list[x] == search else my_list[x]
             for x in range(len(my_list))]
    return(nlist)
