#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create an engine connected to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    try:
        # Query all State objects with a name containing the letter 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete each State object found
        for state in states_to_delete:
            session.delete(state)

        # Commit the session to save the changes
        session.commit()

    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    
    finally:
        # Close the session
        session.close()
