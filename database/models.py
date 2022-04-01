from ast import Str
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  favorites = relationship('Favorite', backref='user')

class Favorite(Base):
  __tablename__ = 'favorite'

  id = Column(Integer, primary_key=True, autoincrement=True)
  symbol = Column(String)
  user_id = Column(Integer, ForeignKey('user.id'))