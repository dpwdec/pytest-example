from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" Setup db connection"""
db = create_engine("postgres://dec@localhost/pytestdb_test")

Session = sessionmaker(db)

""" Create Base ORM model class """
Base = declarative_base()