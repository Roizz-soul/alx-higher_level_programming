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
    sql = "SELECT * FROM states WHERE states.name LIKE BINARY '{}'\
           ORDER BY states.id ASC".format(sys.argv[4])
    cur = db.cursor()
    cur.execute(sql)
    for i in cur.fetchall():
        print(i)
    cur.close()
    db.close()
