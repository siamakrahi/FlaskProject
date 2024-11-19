from sqlalchemy import Column, Integer, String, Text, Boolean
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    fname = sa.Column(sa.String(50), nullable=False)
    lname = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(255), nullable=False, unique=True)
    password = sa.Column(sa.String(255), nullable=False)
    role = sa.Column(sa.String(50), default='user')


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    message = Column(Text, nullable=False)


class HelpRequest(Base):
    __tablename__ = "helprequest"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)


class Newsletter(Base):
    __tablename__ = "newsletter"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    




