#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This example shows how to use ppsql to print a SQLAlchemy query as an SQL
string.
"""
from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )


def create_database():
    engine = create_engine("sqlite://", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")
    mj_user = User(name="mary", fullname="Mary Jones", nickname="marysnickname")
    aj_user = User(name="anne", fullname="Anne Jones", nickname="annesnickname")

    session.add_all([ed_user, mj_user, aj_user])

    return session


if __name__ == "__main__":
    from ppsql import sqlalchemy_ppsql as ppsql

    session = create_database()

    print("simple filter for 'mary'")
    query = session.query(User).filter(User.name == "mary")
    ppsql(query, dialect="sqlite")

    print("\n\nfiltering with `in_`")
    query = session.query(User).filter(User.name.in_(("mary", "anne")))
    ppsql(query, dialect="sqlite")
