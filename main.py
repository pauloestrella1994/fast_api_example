from fastapi import FastAPI, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from models.books import Books

from models.student import Student, UpdateStudent
from models.books import Books


app = FastAPI()

students = {
  1: {
    "name": "John",
    "age": 17,
    "year": "year 12"
  }
}

@app.get("/")
async def root():
  return 'Hello World'

@app.get("/get-student/{student_id}")
async def get_student(student_id: int = Path(None, description="The id of the student", gt = 0, lt = 3)):
  return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
  for student_id in students:
    if students[student_id]["name"] == name:
      return students[student_id]
  return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
  if student_id in students:
    return {"Error": "Student exists"}

  students[student_id] = student
  return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
  if student_id not in students:
    return {"Error": "Student not exists"}

  students[student_id] = student
  return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
  if student_id not in students:
    return {"Error": "Student not exists"}

  del students[student_id]
  return {"Message": "Student deleted"}


@app.post("/books")
def create_books(book: Books):
  to_create = Books(
    title=book.title, 
    description=book.description
  )
  return JSONResponse(status_code=200, content=jsonable_encoder(to_create))
