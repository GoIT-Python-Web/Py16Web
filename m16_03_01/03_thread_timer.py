from threading import Timer
import logging
from time import sleep


def worker(param):
    logging.info(param)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    one = Timer(0.5, worker, args=("one",))
    one.name = "First thread"
    one.start()

    two = Timer(1.5, worker, args=("two",))
    two.name = "Second thread"
    two.start()

    sleep(1)

    one.cancel()
    two.cancel()
    logging.info("End program")
