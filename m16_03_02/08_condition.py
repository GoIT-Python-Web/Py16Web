import sys
from multiprocessing import Process, Condition
from time import sleep


def worker(condition: Condition):
    print("Run event work. Wait...")
    with condition:
        condition.wait()
        print("The owner gave Doby a sock! Can work")
        sys.exit(0)


def master(condition: Condition):
    print("Master does the hard work")
    with condition:
        print("We give permission for others to work")
        condition.notify_all()
        sys.exit(0)


if __name__ == "__main__":
    condition = Condition()
    master_one = Process(name="master", target=master, args=(condition,))

    worker_one = Process(target=worker, args=(condition,))
    worker_two = Process(target=worker, args=(condition,))
    worker_one.start()
    worker_two.start()

    sleep(5)
    master_one.start()

    print("End program")
