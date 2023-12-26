from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Todo, User
from src.schemas.todo import TodoSchema, TodoUpdateSchema


async def get_todos(limit: int, offset: int, db: AsyncSession, user: User):
    """
    The get_todos function returns a list of todos for the user.

    :param limit: int: Limit the number of todos returned
    :param offset: int: Skip the first n results
    :param db: AsyncSession: Pass a database connection to the function
    :param user: User: Filter the todos by user
    :return: A list of todo objects
    :doc-author: Trelent
    """
    stmt = select(Todo).filter_by(user=user).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_all_todos(limit: int, offset: int, db: AsyncSession):
    """
    The get_all_todos function returns a list of all todos in the database.

    :param limit: int: Limit the number of todos returned
    :param offset: int: Specify how many rows to skip
    :param db: AsyncSession: Pass the database connection to the function
    :return: A list of todo objects
    :doc-author: Trelent
    """
    stmt = select(Todo).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_todo(todo_id: int, db: AsyncSession, user: User):
    """
    The get_todo function takes in an id, and returns the todo object with that id.

    :param todo_id: int: Specify the id of the todo to get
    :param db: AsyncSession: Pass the database session to the function
    :param user: User: Get the user who created the todo
    :return: A todo object
    """
    stmt = select(Todo).filter_by(id=todo_id, user=user)
    todo = await db.execute(stmt)
    return todo.scalar_one_or_none()


async def create_todo(body: TodoSchema, db: AsyncSession, user: User):
    todo = Todo(**body.model_dump(exclude_unset=True), user=user)  # (title=body.title, description=body.description)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def update_todo(todo_id: int, body: TodoUpdateSchema, db: AsyncSession, user: User):
    stmt = select(Todo).filter_by(id=todo_id, user=user)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()
    if todo:
        todo.title = body.title
        todo.description = body.description
        todo.completed = body.completed
        await db.commit()
        await db.refresh(todo)
    return todo


async def delete_todo(todo_id: int, db: AsyncSession, user: User):
    stmt = select(Todo).filter_by(id=todo_id, user=user)
    todo = await db.execute(stmt)
    todo = todo.scalar_one_or_none()
    if todo:
        await db.delete(todo)
        await db.commit()
    return todo
