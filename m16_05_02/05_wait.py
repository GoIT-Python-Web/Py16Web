import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError

from timing import async_timed, sync_timed

urls = [
    "https://github.com",
    "https://www.codewars.com",
    "https://rezka.cc/",
    "https://hltv.org/",
    "https://app.amplitude.com/",
    "https://www.youtube.com/",
    "https://tabletki.ua",
    "asdf",
    "ws://test.com",
    "https://stackoverflow.com/",
]


def get_preview(url: str) -> tuple[str, str] | None:
    try:
        res = requests.get(url)
        return url, res.text[:25]
    except (InvalidSchema, MissingSchema, SSLError) as err:
        return None


@async_timed()
async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        done, pending = await asyncio.wait(futures, return_when=asyncio.ALL_COMPLETED)
        print('Done: ', done)
        print('Pending: ', pending)
        [task.cancel() for task in pending]
        result = []
        for task in done:
            result.append(await task)
        return result


@async_timed()
async def main_err():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        done, pending = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
        print('Done: ', done)
        print('Pending: ', pending)
        [task.cancel() for task in pending]
        result = []
        for task in done:
            try:
                result.append(await task)
            except Exception as err:
                print(err)
        return result


if __name__ == "__main__":
    r: list = asyncio.run(main())
    print(r)

    r: list = asyncio.run(main_err())
    print(r)

