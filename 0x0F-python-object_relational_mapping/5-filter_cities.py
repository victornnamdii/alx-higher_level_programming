#!/usr/bin/python3
"""
File: 5-filter_cities.py
Author: Ildoiuba Victor
Desc: a script that takes in the name of a state as an argument and lists
        all cities of that state, using the database hbtn_0e_4_usa.
Date: 07 Oct 2022
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id\
                        WHERE BINARY states.name=%s ORDER BY cities.id ASC",
                   (argv[4],))
    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    cursor.close()
    db.close()
