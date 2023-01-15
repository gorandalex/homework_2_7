from faker import Faker

from database.db import session, NUMBER_TEACHERS
from database.models import Teacher

fake = Faker('uk_UA')


def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            firstname=fake.first_name(),
            lastname = fake.last_name(),
            
        )
        session.add(teacher)

    session.commit()


if __name__ == '__main__':
    create_teachers()