#!/usr/bin/python3
"""
Module that lists all cities of a given state
from the database hbtn_0e_4_usa (safe from SQL injection).
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL database and lists all cities
    of the provided state name (using parameterized queries).
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

    query = ("SELECT cities.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
