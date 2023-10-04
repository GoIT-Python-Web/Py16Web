import sys
from multiprocessing import Process, Event
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        print('Run event work')

        if event_for_exit.is_set():
            sys.exit(0)


if __name__ == '__main__':
    event = Event()
    pr = Process(target=example_work, args=(event,))
    pr.start()

    sleep(5)
    event.set()

    print('End program')
