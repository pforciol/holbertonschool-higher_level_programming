#!/usr/bin/python3
"""
Script that prints the `State` object in `hbtn_0e_0_usa`
where `name` matches the argument `state name to search`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    st_name = sys.argv[4]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    q = session.query(State).filter(State.name == st_name).order_by(State.id)

    if q.first():
        print(q.first().id)
    else:
        print("Not found")
