#!/usr/bin/python3
"""
File: 1-write_file.py
Desc: This module contains one function;
write_file(filename="", text="")
Author: Ilodiuba Victor (victornnamdii)
Date Created: 02 Aug 2022
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return(f.write(text))
