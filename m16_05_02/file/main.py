"""
Відсортувати файли в теці.
"""

import argparse
import asyncio
import logging

from aiopath import AsyncPath
from aioshutil import copyfile

"""
--source [-s] 
--output [-o] default folder = dist
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = AsyncPath(args.get("source"))
output = AsyncPath(args.get("output"))

folders = []


async def read_folder(path: AsyncPath) -> None:
    async for el in path.iterdir():
        if await el.is_dir():
            await read_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath) -> None:
    ext = file.suffix[1:]
    ext_folder = output / ext
    try:
        await ext_folder.mkdir(exist_ok=True, parents=True)
        await copyfile(file, ext_folder / file.name)
    except OSError as err:
        logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    asyncio.run(read_folder(source))
