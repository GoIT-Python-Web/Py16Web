from random import randint
from threading import Thread, RLock
import logging
from time import sleep

counter = 0
lock = RLock()


def worker():
    global counter
    while True:
        # lock.acquire()
        with lock:
            counter += 1
            sleep(randint(1, 2))
            with open("result.txt", "a") as fd:
                fd.write(f"{counter}\n")
        # lock.release()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.info("Starting")
    for i in range(5):
        th = Thread(target=worker, name=f"Thread#{i}")
        th.start()
    logging.info("End program")
