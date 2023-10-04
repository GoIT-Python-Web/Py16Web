from multiprocessing import Process, Queue
from time import sleep
import sys


def worker(qu: Queue, name):
    print(f"{name} started!")
    val = qu.get()
    print(f"{name} {val ** 2}")
    sys.exit(0)  # Якщо не нуль, то це код помилки


if __name__ == "__main__":
    qu = Queue()

    pr1 = Process(target=worker, args=(qu, "first"))
    pr2 = Process(target=worker, args=(qu, "second"))

    pr1.start()
    pr2.start()

    qu.put(10)
    qu.put(5)
    qu.put(15)  # ніхто мене не лове
    sleep(0.5)
    print(qu.empty())
