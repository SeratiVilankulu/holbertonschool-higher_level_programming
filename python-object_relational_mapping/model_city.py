#!/usr/bin/python3
"""
Defines the City class which links to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

# Define the City class which will be linked to the 'cities' table
class City(Base):
    __tablename__ = 'cities'

    # Define the columns in the 'cities' table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
