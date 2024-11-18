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
