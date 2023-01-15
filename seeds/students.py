from faker import Faker
import random

from database.db import session, NUMBER_STUDENTS
from database.models import Student, Group

fake = Faker('uk_UA')


def create_students():
    groups = session.query(Group).all()
    
    for _ in range(NUMBER_STUDENTS):
        group = random.choice(groups)
        
        student = Student(
            firstname=fake.first_name(),
            lastname = fake.last_name(),
            group_id = group.id
        )
        session.add(student)

    session.commit()


if __name__ == '__main__':
    create_students()