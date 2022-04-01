from pydantic import BaseModel
from typing import List


class UserSchema(BaseModel):
  name: str

class Standard(BaseModel):
  message: str

class Error(Standard):
  details: str

class Favorite(BaseModel):
  user_id: int
  symbol: str

class Favorites(BaseModel):
  id: int
  symbol: str
  user_id: int

  class Config:
    orm_mode = True

class ListUsers(BaseModel):
  id: int
  name: str
  favorites: List[Favorites]

  class Config:
    orm_mode = True

class DaySummary(BaseModel):
  highest: float
  lowest: float
  symbol: str
