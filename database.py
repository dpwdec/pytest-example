from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import ActiveRecordMixin

""" Setup db connection"""
db = create_engine("postgres://dec@localhost/pytestdb_test")

Session = sessionmaker(db)

""" Create Base ORM model class """
Base = declarative_base()

class BaseModel(Base, ActiveRecordMixin):
    __abstract__ = True
    pass

