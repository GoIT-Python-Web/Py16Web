import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Student, Contact


fake = Faker('uk-UA')


def insert_contacts():
    students = session.query(Student).all()

    for _ in range(len(list(students)) + 7):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            student_id=random.choice(students).id
        )
        session.add(contact)


if __name__ == '__main__':
    try:
        insert_contacts()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
