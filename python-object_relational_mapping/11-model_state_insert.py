#!/usr/bin/python3
"""
Module that adds the State object "Louisiana" to the database
using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Connects to MySQL database and adds a new State object
    with the name "Louisiana".
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
