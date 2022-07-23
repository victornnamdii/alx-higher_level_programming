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
    m = "z"
    k = 1
    for letter in text:
        if (k == 1 and letter == " "):
            continue
        else:
            k = 2
        if not (letter == " " and m in ".?:"):
            print(letter, end="")
        if letter in ".?:":
            print("\n" * 2, end="")
            k = 1
        m = letter
