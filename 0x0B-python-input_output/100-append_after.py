#!/usr/bin/python3
"""
File: 100-append_after.py
Desc: This module contains a function;
append_after(filename="", search_string="", new_string="")
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string
    """
    line_list = []
    with open(filename, "r", encoding="UTF-8") as f:
        line_list = f.readlines()
        i = 0
        while i < len(line_list):
            if search_string in line_list[i]:
                line_list[i:i + 1] = [line_list[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(line_list)
