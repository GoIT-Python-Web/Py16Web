from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine, join
from sqlalchemy.sql import select

metadata = MetaData()

engine = create_engine("sqlite:///:memory:", echo=True)

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('email', String, nullable=False),
                  Column('user_id', Integer, ForeignKey('users.id'))
                  )

metadata.create_all(engine)


if __name__ == '__main__':
    with engine.connect() as conn:
        ins_user = users.insert().values(fullname='Jack Jones')
        print(ins_user)
        result = conn.execute(ins_user)
        jones_id = result.lastrowid
        print(jones_id)
        ins_user = users.insert().values(fullname='Vasya Pupkin')
        print(ins_user)
        result = conn.execute(ins_user)
        pupkin_id = result.lastrowid
        print(pupkin_id)

        result = conn.execute(select(users))
        for row in result:
            print(row)

        ins_address = addresses.insert().values(email='jones@email.com', user_id=jones_id)
        conn.execute(ins_address)
        ins_address = addresses.insert().values(email='pupkin@email.com', user_id=pupkin_id)
        conn.execute(ins_address)

        result = conn.execute(select(addresses))
        for row in result:
            print(row)

        sql_select = select(users.c.id, addresses.c.email, users.c.fullname).join(users)
        result = conn.execute(sql_select)
        for row in result:
            print(row)
