from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.books import Books

from models.books import Books


app = FastAPI()


@app.post("/books")
def create_books(book: Books):
  to_create = Books(
    title=book.title, 
    description=book.description
  )
  return JSONResponse(status_code=200, content=jsonable_encoder(to_create))
