from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Books(Base):
  __tablename__ = 'books'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  description = Column(String, nullable=False)
