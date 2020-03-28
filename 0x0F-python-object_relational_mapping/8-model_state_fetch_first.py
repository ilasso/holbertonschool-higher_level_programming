#!/usr/bin/python3
"""
Module:8-model_state_fetch_first
       select first state through sqlalchemy
       if doesnt have states print Nothing
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
    stat = session.query(State).first()
    if stat is None:
        print("Nothing")
    else:
        print(str(stat.id)+": "+stat.name)
