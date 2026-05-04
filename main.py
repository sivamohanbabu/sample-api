from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message":"Hello,Fast API"}

@app.get("/students/{id}")
def get_student(id:int):
    return {"student_id",id}