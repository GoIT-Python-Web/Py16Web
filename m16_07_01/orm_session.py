from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, join
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///:memory:", echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    fullname = Column('fullname', String)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(50), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship('User')


Base.metadata.create_all(engine)

if __name__ == '__main__':
    n_user = User(fullname='Jack Jones')
    session.add(n_user)
    n_address = Address(email='jones@email.com', user=n_user)
    session.add(n_address)
    session.commit()

    users = session.query(User).all()
    for row in users:
        print(row.id, row.fullname)

    user = session.query(User).filter_by(id=1).first()
    print(user.fullname)

    address = session.query(Address).first()
    print(address.email)

    session.close()
