from fastapi import FastAPI, Path

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
