from http.client import responses
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from database.models import User
from service import UserService
from schemas import User, Standard, AlternativeOutput


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse("root.html", {"request": request})

@app.post('/user/create', description="Create User",response_model=Standard, responses={418: {'model': AlternativeOutput}})
async def create_user(user: User):
  try:
    await UserService.create_user(name=user.name)
    return Standard(message="Ok")
  except:
    pass
