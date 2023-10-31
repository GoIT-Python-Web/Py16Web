from sqlalchemy import Integer, String, ForeignKey, create_engine, select, and_, or_, not_, desc, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column

engine = create_engine("sqlite:///:memory:", echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(120))


class Address(Base):
    __tablename__ = 'addresses'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship('User')


Base.metadata.create_all(engine)

if __name__ == '__main__':
    n_user = User(fullname='Jack Jones')
    session.add(n_user)
    n_address = Address(email='jones@email.com', user=n_user)
    session.add(n_address)
    n_address = Address(email='jones_next@email.com', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Senior Pomidor')
    session.add(n_user)
    n_address = Address(email='senior@email.com', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Senior Горох')
    session.add(n_user)
    n_address = Address(email='g_senior@email.com', user=n_user)
    session.add(n_address)
    n_address = Address(email='senior_goroh@email.com', user=n_user)
    session.add(n_address)
    n_address = Address(email='goroh_senior@email.com', user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname='Adam Smith')
    session.add(n_user)
    n_address = Address(email='adam@email.com', user=n_user)
    session.add(n_address)
    session.commit()

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement = select(Address.id, Address.email, User.fullname).join(Address.user)
    for row in session.execute(statement):
        print(row)

    print('--------------------------ALL and Scalars--------------------------------------')
    statement = select(User)
    columns = ["id", "fullname"]
    result = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in session.execute(statement).all()]
    print(result)

    result = [dict(zip(columns, (row.id, row.fullname))) for row in session.execute(statement).scalars()]
    print(result)
    print('----------------------------------------------------------------')

    statement = select(User).where(User.fullname == 'Senior Pomidor')
    r = session.execute(statement).scalar_one_or_none()
    if r:
        print(r.fullname)

    # AND
    statement = select(User).where(User.fullname.like('Senior%')).where(User.id == 3)
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    # AND
    statement = select(User).where(and_(User.fullname.like('Senior%'), User.id == 3))
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    # OR
    statement = select(User).where(or_(User.fullname.like('Senior%'), User.id == 1))
    r = session.execute(statement).scalars()
    for row in r:
        print(row.fullname)

    statement = select(User).order_by(desc(User.fullname))
    columns = ["id", "fullname"]
    result = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in session.execute(statement)]
    print(result)

    statement = (
        select(User.fullname, func.count(Address.id))
        .join(Address)
        .group_by(User.fullname)
    )
    result = session.execute(statement).all()
    for fullname, count in result:
        print(f"{fullname}: {count}")

    statement = (
        select(User.fullname, func.count(Address.id))
        .join(Address)
        .group_by(User.fullname)
    )
    result = session.execute(statement).mappings()
    for row in result:
        print(row)

    session.close()
