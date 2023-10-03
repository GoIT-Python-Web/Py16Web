from threading import Event, Thread
from time import sleep
import logging


def worker(event: Event, event_for_exit: Event):
    while True:
        if event_for_exit.is_set():
            break

        sleep(1)
        if event.is_set():
            logging.info("Холостий ход")
            continue
        else:
            logging.info("DDOS server")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    event_exit = Event()

    th = Thread(target=worker, args=(event, event_exit))
    th.start()

    logging.info("Start program")
    sleep(2)
    event.set()  # зупинити виконання потоку
    logging.info("Stop thread")
    sleep(2)
    event.clear()
    logging.info("Start thread")
    sleep(3)
    event_exit.set()
    logging.info("End program")
