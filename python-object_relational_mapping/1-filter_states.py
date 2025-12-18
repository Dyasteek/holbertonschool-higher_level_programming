#!/usr/bin/python3
"""
Module that lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL database and lists all states
    whose name starts with 'N' (case-sensitive).
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
