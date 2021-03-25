#!/usr/bin/python3
"""This is the State module.

Contains the State class that inherits from Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class links to the `states` table of our database.

    Attributes:
        id (int): id of the state.
        name (str): name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
