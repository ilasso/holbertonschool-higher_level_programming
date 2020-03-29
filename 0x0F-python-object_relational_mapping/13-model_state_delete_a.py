#!/usr/bin/python3
"""
Module:13-model_state_delete_a
       delete state tha contains "a" char in name
"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import State, Base


if __name__ == "__main__":

    engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2],
                                                         argv[3]),
             pool_pre_ping=True)

    session = Session(engine)

    for i in session.query(State).filter(State.name.like('%a%')):
        session.delete(i)

    session.commit()

    session.close()
