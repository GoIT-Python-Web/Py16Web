import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from fastapi_users import schemas

from src.entity.models import Role


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    username: str
