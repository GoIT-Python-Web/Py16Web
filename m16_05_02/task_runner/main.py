import asyncio
import logging

from aiopath import AsyncPath
from aiofile import async_open


async def producer(file: AsyncPath, q: asyncio.Queue):
    print("start", file.name)
    async with async_open(file, 'r', encoding='utf-8') as afd:
        data = []
        async for line in afd:
            data.append(str(line))
        await q.put((file, "".join(data)))
    print("end", file.name)


async def consumer(filename, q: asyncio.Queue):
    async with async_open(filename, 'w', encoding='utf-8') as afd:
        while True:
            file, blob = await q.get()
            await afd.write(f"{blob}\n")
            q.task_done()


async def main():

    queue_files = asyncio.Queue()
    list_files = AsyncPath(".").joinpath("files").glob("*.js")

    producer_tasks = [asyncio.create_task(producer(file, queue_files)) async for file in list_files]
    consumer_task = asyncio.create_task(consumer("main.js", queue_files))

    await asyncio.gather(*producer_tasks)
    await queue_files.join()
    consumer_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())




