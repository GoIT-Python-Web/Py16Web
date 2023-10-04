"""
Відсортувати файли в папці.
"""

import argparse
import sys
from multiprocessing import Pool, cpu_count
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
--source [-s] 
--output [-o] default folder = dist
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())
source = Path(args.get("source"))
output = Path(args.get("output"))


def grabs_folder(path: Path) -> list[Path]:
    folders = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            inner_dir = grabs_folder(el)
            if len(inner_dir):
                folders = folders + inner_dir
    return folders


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)
                sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders = [source, *grabs_folder(source)]  # ['picture', 'icons', 'Logo', ...]
    # folders = [source] + grabs_folder(source)

    with Pool(cpu_count()) as pool:
        pool.map(copy_file, folders)
        pool.close()
        pool.join()

    print(f"Можна видалять {source}")
