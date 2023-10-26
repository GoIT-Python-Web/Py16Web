import logging

from psycopg2 import DatabaseError

from connect import create_connection

if __name__ == '__main__':
    sql_expression_01 = """
        SELECT * FROM users WHERE id = %s;
        """
    sql_expression_02 = """
        SELECT id, name, email, age 
        FROM users 
        WHERE age >= 27 AND age <= 60
        ORDER BY age desc
        LIMIT 15;
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_01, (13,))
                    print(c.fetchone())
                    c.execute(sql_expression_02)
                    result = c.fetchall()
                    print(result)
                    print(result)
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)