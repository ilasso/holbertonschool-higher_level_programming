#!/usr/bin/python3
"""
Module:9-model_state_filter_a
       select all states names that contains "a" char through sqlalchemy
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
        print(str(i.id)+": "+i.name)
