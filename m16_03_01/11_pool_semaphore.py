from random import randint
from threading import Semaphore, Thread, RLock, current_thread, Lock
from time import sleep
import logging


class Logger:
    def __init__(self):
        self.active = []
        self.lock = RLock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.info(
                f"Почав роботу поток {name}. Зараз в пуле потоки: {self.active}"
            )

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.info(
                f"Закінчив роботу поток {name}. Зараз в пуле потоки: {self.active}"
            )


def worker(semaphore: Semaphore, log: Logger):
    logging.info("waiting...")
    with semaphore:
        name = current_thread().name
        log.make_active(name)
        logging.info("Got semaphore")
        sleep(randint(1, 3))
        logging.info("Finished operation")
        log.make_inactive(name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    pool = Semaphore(3)
    logger = Logger()

    for i in range(7):
        w = Thread(target=worker, args=(pool, logger))
        w.start()
