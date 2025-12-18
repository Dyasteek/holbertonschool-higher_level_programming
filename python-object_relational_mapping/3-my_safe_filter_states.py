#!/usr/bin/python3
"""
Module that displays all values in the states table
where name matches the user input argument (safe from SQL injection).
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL database and displays states
    matching the provided state name (using parameterized queries).
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

