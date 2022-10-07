#!/usr/bin/python3
"""
File: 2-my_filter_states.py
Author: Ildoiuba Victor
Desc: a script that takes in an argument and displays all values in the states
        table of hbtn_0e_0_usa where name matches the argument.
Date: 06 Oct 2022
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name='{}'\
                    ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
