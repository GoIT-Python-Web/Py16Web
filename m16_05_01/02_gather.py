import asyncio
from time import sleep, time

from faker import Faker

fake = Faker("uk-UA")  # en-GB


def get_user_from_db(uuid: int):
    sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.user_name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 6):
        users.append(async_get_user_from_db(i))
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    start = time()
    for i in range(1, 6):
        user = get_user_from_db(i)
        print(user)
    print(time() - start)

    start = time()
    users = asyncio.run(main())
    print(users)
    print(time() - start)
