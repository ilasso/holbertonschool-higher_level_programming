#!/usr/bin/python3
"""
Module:11-model_state_insert
       insert a new state(lousiana) print new id
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

    statetoins = State(name='Louisiana')

    session.add_all([statetoins])

    session.commit()

    print(statetoins.id)

    session.close()
