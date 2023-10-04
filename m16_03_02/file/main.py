"""
Відсортувати файли в папці.
"""

import argparse
import logging
from pathlib import Path
from shutil import copyfile
from queue import Queue
from threading import Thread, Condition
from time import sleep

from progress.bar import Bar, ShadyBar

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
bar = None


def master(path: Path):
    global bar
    grabs_folder(path)
    logging.info("Completed grabs folder")
    with condition:
        bar = ShadyBar('Processing', max=len(folders.queue), suffix='%(percent)d%%')
        condition.notify_all()


def grabs_folder(path: Path) -> None:
    logging.info(f"Start grabs folder {path}")
    for el in path.iterdir():
        if el.is_dir():
            folders.put(el)
            grabs_folder(el)


def copy_file() -> None:
    logging.info('Wait...')
    with condition:
        condition.wait()
    while not folders.empty():
        path = folders.get()
        bar.next()
        for el in path.iterdir():
            if el.is_file():
                ext = el.suffix[1:]
                ext_folder = output / ext
                try:
                    ext_folder.mkdir(exist_ok=True, parents=True)
                    copyfile(el, ext_folder / el.name)
                except OSError as err:
                    logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    condition = Condition()
    folders = Queue()

    folders.put(source)

    master_grabs = Thread(target=master, args=(source,))
    master_grabs.start()

    threads = []
    for i in range(3):
        th = Thread(target=copy_file)
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"\nМожна видалять {source}")
