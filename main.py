from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
  1: {
    "name": "John",
    "age": 17,
    "class": "year 12"
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
