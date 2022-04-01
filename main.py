from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List

from database.models import User
from service import FavoriteService, UserService
from schemas import ListUsers, User, Standard, Error, Favorite


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse("root.html", {"request": request})

@app.post('/user/create', description="Create User", response_model=Standard, responses={400: {'model': Error}})
async def create_user(user: User):
  try:
    await UserService.create_user(name=user.name)
    return Standard(message="Ok")
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@app.delete('/delete/user/{user_id}', description="Delete User", response_model=Standard, responses={400: {'model': Error}})
async def create_user(user_id: int):
  try:
    await UserService.delete_user(user_id)
    return Standard(message="Ok")
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@app.post('/favorite/add', description="Add Favorite", response_model=Standard, responses={400: {'model': Error}})
async def add_favorite(favorite: Favorite):
  try:
    await FavoriteService.add_favorite(user_id=favorite.user_id, symbol=favorite.symbol)
    return Standard(message="Ok")
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@app.delete('/delete/favorite/{user_id}', description="Delete Favorite", response_model=Standard, responses={400: {'model': Error}})
async def favorite_delete(user_id: int, symbol: str):
  try:
    await FavoriteService.delete_favorite(user_id=user_id, symbol=symbol)
    return Standard(message="Ok")
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@app.post('/users/', description="List Users", response_model=List[ListUsers], responses={400: {'model': Error}})
async def get_users():
  try:
    return await UserService.list_user()
  except Exception as error:
    raise HTTPException(400, detail=str(error))
