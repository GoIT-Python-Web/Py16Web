from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Todo, User
from src.schemas.todo import TodoSchema, TodoUpdateSchema


async def get_todos(limit: int, offset: int, db: AsyncSession, user: User):
    stmt = select(Todo).filter_by(user=user).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_all_todos(limit: int, offset: int, db: AsyncSession):
    stmt = select(Todo).offset(offset).limit(limit)
    todos = await db.execute(stmt)
    return todos.scalars().all()


async def get_todo(todo_id: int, db: AsyncSession, user: User):
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
