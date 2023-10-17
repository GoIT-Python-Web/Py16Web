import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def read_file():
    with open(__file__, "r") as f:
        return f.read(100)


def calculate(power: int, p: int):
    r = [i**power for i in range(10**p)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        f = await loop.run_in_executor(pool, read_file)
        print(f)

    with ProcessPoolExecutor() as pool:
        f = await loop.run_in_executor(pool, calculate, 20, 5)
        print(f)


if __name__ == "__main__":
    asyncio.run(main())
