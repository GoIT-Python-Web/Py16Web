import asyncio
import random


async def ping(signal):
    print(f"Pinging {signal}")


async def boo():
    print(f"RUN  BOO")


async def main():
    while True:
        await asyncio.sleep(1)
        await ping(random.randint(1, 1000))


if __name__ == "__main__":
    # asyncio.run(main())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    loop.create_task(boo())
    loop.run_forever()
