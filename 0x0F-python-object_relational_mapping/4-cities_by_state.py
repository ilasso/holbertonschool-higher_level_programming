#!/usr/bin/python3
"""
module:4-cities_by_state
description: use MySQLdb package to access db and display all cities
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
    numrows = cursor.execute("SELECT cities.id, cities.name,states.name FROM cities, states\
                              WHERE cities.state_id=states.id\
                              ORDER BY cities.id ASC")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    db.close()
