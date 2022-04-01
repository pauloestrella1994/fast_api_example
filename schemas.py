from email import message
from pydantic import BaseModel


class User(BaseModel):
  name: str

class Standard(BaseModel):
  message: str

class AlternativeOutput(Standard):
  details: str
