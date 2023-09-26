from typing import TypedDict, Literal, NamedTuple
from dataclasses import dataclass


class UserInfo(TypedDict):
    id: int
    username: str
    email: str
    is_active: bool


@dataclass(frozen=True)
class UserSchema:
    id: int
    username: str
    email: str
    is_active: bool = True


class Cat(NamedTuple):
    nick: str
    age: int


User = {"id": 123, "username": "Dmitro", "email": "dmitro@gmail.com", "is_active": True}


def get_user() -> UserInfo:
    return User


def get_user_info() -> UserSchema:
    return UserSchema(id=123, username="Dmitro", email="dmitro@gmail.com")


def my_mul(data: list) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


Shape = Literal["circle", "square"]


def foo(shape: Shape):
    if shape == "circle":
        print("It is a circle")
    elif shape == "square":
        print("It is a square")


if __name__ == "__main__":
    my_mul([2])
    print(get_user()["username"])
    foo("circle")
    cat = Cat(nick="Simon", age=5)
    print(cat.nick)
