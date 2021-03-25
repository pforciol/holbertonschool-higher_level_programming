#!/usr/bin/python3
"""
Script that creates the `State` “California” with the
`City` “San Francisco” from the database `hbtn_0e_100_usa`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    newState = State(name="California")
    newState.cities.append(City(name="San Francisco"))

    session.add(newState)
    session.commit()
