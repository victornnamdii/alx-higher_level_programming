#!/usr/bin/python3
"""
File: 0-select_states.py
Author: Ildoiuba Victor
Desc: a script that lists all states from the database hbtn_0e_0_usa
Date: 06 Oct 2022
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
