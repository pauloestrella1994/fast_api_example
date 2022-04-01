from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from database.models import User
from service import UserService
from schemas import User, Standard, Error


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

@app.delete('/delete/{user_id}', description="Delete User", response_model=Standard, responses={400: {'model': Error}})
async def create_user(user_id: int):
  try:
    await UserService.delete_user(user_id)
    return Standard(message="Ok")
  except Exception as error:
    raise HTTPException(400, detail=str(error))
