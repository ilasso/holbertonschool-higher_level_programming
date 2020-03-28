#!/usr/bin/python3
"""
module:2-my_filter_states
description: use MySQLdb package to access db and display states rows
             where name = argv[4]
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    numrows = cursor.execute("SELECT * FROM states\
                              WHERE BINARY name = '{}'\
                              ORDER BY id ASC".format(argv[4]))
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()
