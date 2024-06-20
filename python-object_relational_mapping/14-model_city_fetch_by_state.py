#!/usr/bin/python3
"""
Fetches and prints all City objects from the database hbtn_0e_14_usa,
sorted by cities.id, in the format <state name>: (<city id>) <city name>.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>")
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
        # Query all City objects and join with State to get the state name
        cities = session.query(City).join(State).order_by(City.id).all()

        # Print the results in the specified format
        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        # Close the session
        session.close()
