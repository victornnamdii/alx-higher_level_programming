#!/usr/bin/python3
"""
File: 1-my_list.py
Desc: This file contains one class; MyList
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""


class Mylist(list):
    """
    Represents a class MyList
    """

    def print_sorted(self):
        """
        Prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
