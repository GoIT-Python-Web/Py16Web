from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = 'todos'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), index=True)
    description: Mapped[str] = mapped_column(String(250))
    completed: Mapped[bool] = mapped_column(default=False)
