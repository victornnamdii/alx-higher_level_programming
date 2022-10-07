#!/usr/bin/python3
"""
File: 10-model_state_my_get.py
Author: Ildoiuba Victor
Desc: a script that prints the State object with the name passed
        as argument from the database hbtn_0e_6_usa
Date: 07 Oct 2022
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like(argv[4])).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
