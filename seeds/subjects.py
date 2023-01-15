from faker import Faker
import random

from database.db import session, NUMBER_SUBJECTS
from database.models import Subject, Teacher

fake = Faker('uk_UA')


def create_subjects():
    teachers = session.query(Teacher).all()
    
    for _ in range(NUMBER_SUBJECTS):
        teacher = random.choice(teachers)
        
        subject = Subject(
            name=fake.job(),
            teacher_id = teacher.id
        )
        session.add(subject)

    session.commit()


if __name__ == '__main__':
    create_subjects()