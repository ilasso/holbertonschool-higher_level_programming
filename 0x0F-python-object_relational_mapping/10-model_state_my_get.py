#!/usr/bin/python3
"""
Module:10-model_state_my_get
       prints the State object with the name passed as argument argv[4]
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
    obj = session.query(State).filter(State.name == argv[4])\
                              .first()
    if obj is None:
        print("Not found")
    else:
        print(obj.id)
    session.close()
