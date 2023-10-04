from multiprocessing import Process, JoinableQueue
from time import sleep
import sys


def worker(qu: JoinableQueue, name):
    print(f"{name} started!")
    val = qu.get()
    print(f"{name} {val ** 2}")
    sleep(2)
    qu.task_done()
    sys.exit(0)  # Если не ноль, то это код ошибки


if __name__ == "__main__":
    qu = JoinableQueue()

    pr1 = Process(target=worker, args=(qu, "first"))
    pr2 = Process(target=worker, args=(qu, "second"))

    pr1.start()
    pr2.start()

    qu.put(10)
    # sleep(2)
    qu.put(5)
    qu.join()
    print("Finished")
