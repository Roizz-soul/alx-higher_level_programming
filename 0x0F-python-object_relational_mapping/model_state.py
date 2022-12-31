#!/usr/bin/python3
"""
module defines a Class called State
"""

from sqlalchemy import Column, Intger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """creates a class state to represent a table in a database
    Attributes:
        __tablename__: name of the table
        id: state id
        name: state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
