#!/usr/bin/python3
"""
Script that lists all `states` with a name starting
with `N` from the database `hbtn_0e_0_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
