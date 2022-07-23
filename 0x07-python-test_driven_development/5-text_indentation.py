#!/usr/bin/python3
"""
File: 5-text_indentation.py
Desc: This module contains only one function: text_indentation(text)
Author: Ilodiuba Victor (victornnamdii)
Date Created: 23 Jul 2022
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        print(letter, end="")
        if letter is in ".?:":
            print("\n" * 2, end="")
