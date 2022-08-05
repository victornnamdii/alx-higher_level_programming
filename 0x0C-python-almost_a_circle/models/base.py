#!/usr/bin/python3
"""
File: base.py
Desc: THis module contains a class; Base
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

import json

class Base:
    """
    Representation of the class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_to_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        objl = []
        if list_objs is not None:
            for i in list_objs:
                objl.append(cls.to_dictionary(i))
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(cls.to_json_string(objl))
