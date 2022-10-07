#!/usr/bin/python3
"""
File: 14-model_city_fetch_by_state.py
Author: Ildoiuba Victor
Desc: a script that lists all City objects from the
        database hbtn_0e_6_usa
Date: 07 Oct 2022
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).filter(City.state_id == State.id)\
                  .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
