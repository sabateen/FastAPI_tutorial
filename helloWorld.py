from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # السماح بهذه المصادر
    allow_credentials=True,           # هل يتم إرسال الكوكيز أو التوكنات؟
    allow_methods=["*"],              # السماح بكل أنواع الطلبات: GET, POST, PUT...
    allow_headers=["*"],              # السماح بكل أنواع الهيدر
)



class student(BaseModel):
    id: int
    name: str
    grade: int

students= [
    student(id=1, name="marwan sabateen", grade=3),
    student(id=2, name="firas sabateen", grade=5)
        ]
@app.get("/students/")
def read_students():
    return {"students":students}

@app.post("/students/")
def create_student(New_student: student):
    students.append(New_student)
    return(students)


@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: student):
    for index, student in enumerate(students):
        if student.id == student_id: 
            students[index]= update_student
            return update_student
    return{"error":"student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int)
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return{"messege":"student deleted"}
    return{"messege":"student not found"}