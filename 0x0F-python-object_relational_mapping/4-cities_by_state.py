#!/usr/bin/python3
"""
File: 4-cities_by_state.py
Author: Ildoiuba Victor
Desc: a script that lists all cities from the database hbtn_0e_4_usa
Date: 07 Oct 2022
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id ORDER BY \
                    cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
