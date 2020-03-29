#!/usr/bin/python3
"""
Module:model_city
       Create City class based on cities  table desc
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Class:City
          class based on cities table desc
    """
    __tablename__ = "cities"

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey(State.id),
                      nullable=False)
