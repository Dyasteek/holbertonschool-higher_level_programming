#!/usr/bin/python3
"""
Module that prints the State object with the name passed as argument
from the database using SQLAlchemy ORM (safe from SQL injection).
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Connects to MySQL database and prints the State object
    with the provided name (using parameterized queries).
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()


if __name__ == "__main__":
    main()
