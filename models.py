import sqlalchemy as sa 
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy import Enum

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    
    id = sa.Column(sa.Integer,primary_key=True)
    first_name = sa.Column(sa.String(255), nullable=False)
    last_name = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)
    user_request = sa.Column(Enum("Messaging", "Consulting", "Newsletter"))
    avatar = sa.Column(sa.String(255), nullable=True)
    about = sa.Column(sa.Text, nullable=True)


engine = sa.create_engine("sqlite:///myproject.db")

Base.metadata.create_all(engine)
Sessionmaker = sessionmaker(bind=engine)
session = Sessionmaker()
