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
    sql = "SELECT cities.name\
           FROM cities JOIN states\
           WHERE cities.state_id = states.id AND states.name=%s\
           ORDER BY cities.id ASC"
    cur = db.cursor()
    cur.execute(sql, (sys.argv[4],))
    lit = []
    for c in cur.fetchall():
        cit.append(c[0])
    print(", ".join(lit))
    cur.close()
    db.close()
