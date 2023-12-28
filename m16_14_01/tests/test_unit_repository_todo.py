import unittest
from unittest.mock import MagicMock, AsyncMock, Mock

from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Todo, User
from src.schemas.todo import TodoSchema, TodoUpdateSchema
from src.repository.todos import create_todo, get_all_todos, get_todo, update_todo, delete_todo, get_todos


class TestAsyncTodo(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.user = User(id=1, username='test_user', password="qwerty", confirmed=True)
        self.session = AsyncMock(spec=AsyncSession)

    async def test_get_all_todos(self):
        limit = 10
        offset = 0
        todos = [Todo(id=1, title='test_title_1', description='test_description_1', user=self.user),
                 Todo(id=2, title='test_title_2', description='test_description_2', user=self.user)]
        mocked_todos = MagicMock()
        mocked_todos.scalars.return_value.all.return_value = todos
        self.session.execute.return_value = mocked_todos
        result = await get_all_todos(limit, offset, self.session)
        self.assertEqual(result, todos)

    async def test_get_todos(self):
        limit = 10
        offset = 0
        todos = [Todo(id=1, title='test_title_1', description='test_description_1', user=self.user),
                 Todo(id=2, title='test_title_2', description='test_description_2', user=self.user)]
        mocked_todos = Mock()
        mocked_todos.scalars.return_value.all.return_value = todos
        self.session.execute.return_value = mocked_todos
        result = await get_todos(limit, offset, self.session, self.user)
        self.assertEqual(result, todos)

    async def test_create_todo(self):
        body = TodoSchema(title='test_title', description='test_description')
        result = await create_todo(body, self.session, self.user)
        self.assertIsInstance(result, Todo)
        self.assertEqual(result.title, body.title)
        self.assertEqual(result.description, body.description)

    async def test_update_todo(self):
        body = TodoUpdateSchema(title='test_title', description='test_description', completed=True)
        mocked_todo = MagicMock()
        mocked_todo.scalar_one_or_none.return_value = Todo(id=1, title='test_title', description='test_description',
                                                           user=self.user)
        self.session.execute.return_value = mocked_todo
        result = await update_todo(1, body, self.session, self.user)
        self.assertIsInstance(result, Todo)
        self.assertEqual(result.title, body.title)
        self.assertEqual(result.description, body.description)

    async def test_delete_todo(self):
        mocked_todo = MagicMock()
        mocked_todo.scalar_one_or_none.return_value = Todo(id=1, title='test_title', description='test_description',
                                                           user=self.user)
        self.session.execute.return_value = mocked_todo
        result = await delete_todo(1, self.session, self.user)
        self.session.delete.assert_called_once()
        self.session.commit.assert_called_once()

        self.assertIsInstance(result, Todo)
