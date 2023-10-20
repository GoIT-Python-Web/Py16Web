import asyncio
from typing import Iterable, Awaitable, Coroutine, Any

from faker import Faker


from timing import async_timed

fake = Faker("uk-UA")  # en-GB


async def get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def get_users(uuids: list[int]) -> list[Coroutine[int, Any, dict]]:
    return [get_user_from_db(pk) for pk in uuids]


@async_timed("-------------------- main -----------------------")
async def main(users: Coroutine[int, Any, list[Coroutine[int, Any, dict]]]):
    users_ = []
    for user in await users:
        users_.append(user)
    result = await asyncio.gather(*users_)
    return result


if __name__ == "__main__":
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
    