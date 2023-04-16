#!/usr/bin/python3
"""Script that lists all objects from a database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_row = State(name='Louisiana')
    session.add(new_row)
    session.commit()
    res = session.query(State).filter(State.name == 'Louisiana').all()
    if res:
        for i in res:
            print(i.id)
    else:
        print("Not found")
    session.close()
