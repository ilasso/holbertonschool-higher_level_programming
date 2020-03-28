#!/usr/bin/python3
"""
module:5-filter_cities
description: use MySQLdb package to access db and display all cities
             of one specific state
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
    numrows = cursor.execute("SELECT cities.name FROM cities, states\
                              WHERE cities.state_id=states.id and\
                                    states.name = %s\
                              ORDER BY cities.id ASC", (argv[4],))
    lista = []
    for i in cursor.fetchall():
        lista.append(i[0])
    print(", ".join(lista))
    cursor.close()
    db.close()
