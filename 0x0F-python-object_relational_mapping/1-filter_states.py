#!/usr/bin/python3
"""
module:1-filter_states.py
description: use MySQLdb package to access db and display states rows
             where name start with Upper 'N'
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
    numrows = cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in cursor.fetchall():
        if i[1][0] == "N": 
            print(i)
    cursor.close()
    db.close()
