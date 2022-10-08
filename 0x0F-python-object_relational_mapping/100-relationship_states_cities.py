#!/usr/bin/python3
"""
File: 100-relationship_states_cities.py
Author: Ildoiuba Victor
Desc:  a script that creates the State “California” with the City
        “San Francisco” from the database hbtn_0e_100_usa
Date: 07 Oct 2022
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    calif = State(name="California")
    calif.cities = [City(name="San Francisco")]
    session.add(calif)
    session.commit()
    session.close()
