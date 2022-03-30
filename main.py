from fastapi import FastAPI

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
async def get_student(student_id: int):
  return students[student_id]
