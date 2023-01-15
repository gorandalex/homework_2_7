from datetime import datetime
from faker import Faker
import random

from database.db import session, NUMBER_GRADES
from database.models import Grade, Student, Subject

fake = Faker('uk_UA')


def create_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    
    for _ in range(NUMBER_GRADES):
        student = random.choice(students)
        subject = random.choice(subjects)
        
        grade = Grade(
            grade=random.randint(4, 12),
            create_at = fake.date_between_dates(datetime(2022, 9, 1), datetime(2022, 12, 31)),
            student_id = student.id,
            subject_id = subject.id
        )
        session.add(grade)

    session.commit()


if __name__ == '__main__':
    create_grades()