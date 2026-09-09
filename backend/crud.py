from sqlalchemy.orm import Session

from model import Student
from schemas import StudentCreate



def create_student(db:Session, student:StudentCreate):
    db_student = Student(
        name=student.name,
        email=student.email,
        age=student.age,
        course=student.course
    )


    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_student(
    db: Session,
    student_id: int
):

    return db.query(Student).filter(
        Student.id == student_id
    ).first()


def delete_student(
    db: Session,
    student_id: int
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student:

        db.delete(student)
        db.commit()

        return True

    return False