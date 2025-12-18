#!/usr/bin/python3
"""
Module that lists all cities from the database
with their corresponding state names.
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL database and lists all cities
    with their corresponding state names.
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

    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
