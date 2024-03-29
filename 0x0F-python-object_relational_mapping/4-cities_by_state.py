#!/usr/bin/python3
"""Script to list all states from  a database with filter"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities JOIN states\
                 WHERE cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    for c in cur.fetchall():
        print(c)
    cur.close()
    db.close()
