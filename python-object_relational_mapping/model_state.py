#!/usr/bin/python3
"""
Defines the State class and creates a SQLAlchemy ORM model that links to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

class State(Base):
    """
    State class that maps to the 'states' table in the MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Only run the following block if this script is executed directly
if __name__ == "__main__":
    import sys

    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create an engine connected to the specified MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', pool_pre_ping=True)

    # Create all tables in the database (this is equivalent to "CREATE TABLE" in raw SQL)
    Base.metadata.create_all(engine)

