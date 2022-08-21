#!/usr/bin/python3
"""
File: base.py
Desc: THis module contains a class; Base
Author: Ilodiuba Victor (victornnamdii)
Date Created: 04 Aug 2022
"""

import csv
import random
import json
import turtle

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
            list_dictionaries = []
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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            hold = cls(2, 2)
        elif cls.__name__ == "Square":
            hold = cls(2)
        hold.update(**dictionary)
        return hold

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        listo = []
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                listo = cls.from_json_string(f.read())
                for n, objs in enumerate(listo):
                    listo[n] = cls.create(**listo[n])
        except Exception:
            pass
        return listo

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of rectangles/squares as a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding="UTF-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads from csv
        """
        filename = cls.__name__ + ".csv"
        li = []
        try:
            with open(filename, "r", encoding="UTF-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    li.append(obj)
        except Exception:
            pass
        return li

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws the shape on a GUI
        """
        s = turtle.Screen()
        t = turtle.Turtle()
        cl = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        turtle.bgcolor("black")
        t.pensize(3)
        shapes = list_rectangles + list_squares
        for shape in shapes:
            t.pencolor(cl[random.randint(0, 6)])
            t.up()
            t.goto(shape.x, shape.y)
            t.down()
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)

        s.exitonclick()
