#!/usr/bin/python3
"""
Module:model_state
       Create State class based on State table desc
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column


Base = declarative_base()


class State(Base):
    """
    Class:States
          class based on State table desc
    """
    __tablename__ = "states"
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)
