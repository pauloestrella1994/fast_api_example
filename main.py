from fastapi import FastAPI, Path
from typing import Optional

from models.student import Student


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
