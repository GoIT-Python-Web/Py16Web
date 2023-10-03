import pathlib
from queue import Queue
from threading import Thread, Event
import logging


class Writer:
    def __init__(self, filename: str, e: Event):
        self.filename = filename
        self.files_for_handling = Queue()
        self.event = e
        self.file = open(self.filename, "x", encoding="utf-8")

    def __call__(self, *args, **kwargs):
        while True:
            if self.files_for_handling.empty():
                if self.event.is_set():
                    break
            else:
                file, blob = self.files_for_handling.get()
                logging.info(f"Write file {file.name}")
                self.file.write(f"{blob}\n")

    def __del__(self):
        self.file.close()


def reader(files_for_handling: Queue):
    while True:
        if files_for_reading.empty():
            break
        file: pathlib.Path = files_for_reading.get()
        logging.info(f"read file {file.name}")
        with open(file, "r", encoding="utf8") as f:
            data = []
            for line in f:
                data.append(line)
            files_for_handling.put((file, "".join(data)))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    files_for_reading = Queue()
    event = Event()

    list_files = pathlib.Path(".").joinpath("files").glob("*.js")
    print(list_files)
    [files_for_reading.put(file) for file in list_files]
    print(files_for_reading)

    if files_for_reading.empty():
        logging.info("Folder is empty")
    else:
        writer = Writer("main.js", event)
        th_writer = Thread(target=writer, name="Writer")
        th_writer.start()

        threads = []
        for i in range(2):
            tr = Thread(
                target=reader, args=(writer.files_for_handling,), name=f"Reader#{i}"
            )
            tr.start()
            threads.append(tr)

        [th.join() for th in threads]
        event.set()  # файлів для зчитування немає
