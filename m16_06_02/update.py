import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection


fake = Faker('uk-Ua')
COUNT = 5_000


def update_data(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for i in range(COUNT):
            c.execute(sql_expression, (fake.phone_number(), i + 1))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_expression_update = """
        UPDATE users SET phone = %s WHERE id = %s;
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                update_data(conn, sql_expression_update)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
